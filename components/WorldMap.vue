<template>
  <div ref="mapContainer" class="w-full h-full"></div>
</template>

<script>
import mapboxgl from 'mapbox-gl' 
import { h, nextTick, render } from 'vue' 
import CasesLineChart from "~/components/CasesLineChart.vue" 
import '../node_modules/mapbox-gl/dist/mapbox-gl.css' 

let mouseLoc 

export default {
  props: {
    selectedFeature: {
      type: String,
      required: true,
    },
    mapStyle: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      map: null,
      countryCode: null,
      popup: null,
    } 
  },
  mounted() {
    mapboxgl.accessToken = 'pk.eyJ1IjoibWF0YXNhbXUiLCJhIjoiY2x4MnRzOGJqMG1kYTJub21tM3YzZWMyeCJ9.gWwXsEB5lyc3KgDHYYhGLg' 

    this.map = new mapboxgl.Map({
      container: this.$refs.mapContainer,
      style: `mapbox://styles/mapbox/${this.mapStyle}`,
      center: [0, 0],
      zoom: 2,
      interactive: true,
    }) 

    this.map.on('load', () => {
      this.fetchData() 
    }) 

    this.map.on('style.load', () => {
      this.fetchData() 
    }) 

    this.map.on('click', (e) => {
      let features = this.map.queryRenderedFeatures(e.point) 
      let country_code = features[0]?.properties?.ISO_A3 

      mouseLoc = e.lngLat 

      if (!country_code) {
        return 
      }
      this.countryCode = country_code 

      this.showPopup(e.lngLat, country_code) 
    }) 
  },
  watch: {
    selectedFeature() {
      this.updateMap() 
      if (this.countryCode) {
        this.showPopup(mouseLoc, this.countryCode) 
      }
    },
    mapStyle() {  
      this.map.setStyle(`mapbox://styles/mapbox/${this.mapStyle}`) 
    },
  },
  methods: {
    fetchData() {
      fetch('/data.json')
        .then(response => response.json())
        .then(data => {
          this.addSource(data) 
          this.updateMap() 
        })
        .catch(error => {
          console.error('Error fetching data:', error) 
        }) 
    },
    addSource(data) {
      if (!this.map.getSource('countries')) {
        this.map.addSource('countries', {
          type: 'geojson',
          data: data,
        }) 
      }
    },
    updateMap() {
      const propertyMap = {
        Deaths: 'total_deaths',
        Cases: 'total_cases',
        Vaccinations: 'people_vaccinated',
      } 

      const colorScales = {
        Deaths: {
          min: 'hsl(270, 100%, 90%)',
          avg: 'hsl(270, 100%, 57%)',
          max: 'hsl(270, 100%, 25%)',
        },
        Cases: {
          min: 'hsl(100, 100%, 57%)',
          avg: 'hsl(50, 100%, 57%)',
          max: 'hsl(0, 100%, 57%)',
        },
        Vaccinations: {
          min: 'hsl(200, 100%, 90%)',
          avg: 'hsl(200, 100%, 57%)',
          max: 'hsl(200, 100%, 25%)',
        },
      } 

      const property = propertyMap[this.selectedFeature] 
      const colorScale = colorScales[this.selectedFeature] 

      let min = Infinity 
      let max = -Infinity 
      let sum = 0 
      let count = 0 

      this.map.getSource('countries')._data.features.forEach(feature => {
        const value = feature.properties[property] 
        if (value !== undefined && value !== null) {
          min = Math.min(min, value) 
          max = Math.max(max, value) 
          sum += value 
          count++ 
        }
      }) 

      const average = count > 0 ? sum / count : 0 

      if (this.map.getLayer('choropleth')) {
        this.map.removeLayer('choropleth') 
      }

      this.map.addLayer({
        id: 'choropleth',
        type: 'fill',
        source: 'countries',
        paint: {
          'fill-color': [
            'interpolate',
            ['linear'],
            ['get', property],
            min, colorScale.min,
            average, colorScale.avg,
            max, colorScale.max,
          ],
          'fill-opacity': 0.3,
        },
      }) 
    },
    showPopup(lngLat, country_code) {
      if (this.popup) {
        this.popup.remove()
      }

      this.popup = new mapboxgl.Popup()
        .setLngLat(lngLat)
        .setHTML('<div id="line-chart-popup-content"></div>')
        .setMaxWidth("none")
        .addTo(this.map) 

      nextTick(() => {
        const lineChartPopupContent = document.getElementById('line-chart-popup-content') 
        if (lineChartPopupContent) {
        render(h(CasesLineChart, { country_code, selectedFeature: this.selectedFeature }), lineChartPopupContent) 
      }      }) 
    },

  },
} 
</script>
