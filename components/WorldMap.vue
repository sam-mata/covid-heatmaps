<template>
  <div ref="mapContainer" class="w-full h-full"></div>
</template>

<script>
import mapboxgl from 'mapbox-gl';
import data from '../data.js';
import { h, nextTick, render } from 'vue';
import CasesLineChart from "~/components/CasesLineChart.vue";
import '../node_modules/mapbox-gl/dist/mapbox-gl.css';

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
    };
  },
  mounted() {
    mapboxgl.accessToken = 'pk.eyJ1IjoibWF0YXNhbXUiLCJhIjoiY2x4MnRzOGJqMG1kYTJub21tM3YzZWMyeCJ9.gWwXsEB5lyc3KgDHYYhGLg';

    this.map = new mapboxgl.Map({
      container: this.$refs.mapContainer,
      style: `mapbox://styles/mapbox/${this.mapStyle}`,
      center: [0, 0],
      zoom: 2,
      interactive: true,
    });

    this.map.on('load', () => {
      this.addSource();
      this.updateMap();
    });

    this.map.on('style.load', () => {
      this.addSource();
      this.updateMap();
    });

    this.map.on('click', (e) => {
      let features = this.map.queryRenderedFeatures(e.point);
      let country_code = features[0].properties.ISO_A3;

      if (!country_code) {
        return;
      }

      new mapboxgl.Popup()
        .setLngLat(e.lngLat)
        .setHTML('<div id="line-chart-popup-content"></div>')
        .setMaxWidth("none")
        .addTo(this.map);

      nextTick(() => {
        const lineChartPopupContent = document.getElementById('line-chart-popup-content');
        render(h(CasesLineChart, { country_code }), lineChartPopupContent);
      });
    });
  },
  watch: {
    selectedFeature() {
      this.updateMap();
    },
    mapStyle() {
      this.map.setStyle(`mapbox://styles/mapbox/${this.mapStyle}`);
    },
  },
  methods: {
    addSource() {
      if (!this.map.getSource('countries')) {
        this.map.addSource('countries', {
          type: 'geojson',
          data: data,
        });
      }
    },
    updateMap() {
      const propertyMap = {
        Deaths: 'total_deaths',
        Cases: 'total_cases',
        Vaccinations: 'people_vaccinated',
      };

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
      };

      const property = propertyMap[this.selectedFeature];
      const colorScale = colorScales[this.selectedFeature];

      // Calculate min, max, and average values for the selected feature
      let min = Infinity;
      let max = -Infinity;
      let sum = 0;
      let count = 0;

      data.features.forEach(feature => {
        const value = feature.properties[property];
        if (value !== undefined && value !== null) {
          min = Math.min(min, value);
          max = Math.max(max, value);
          sum += value;
          count++;
        }
      });

      const average = count > 0 ? sum / count : 0;

      if (this.map.getLayer('choropleth')) {
        this.map.removeLayer('choropleth');
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
      });
    },
  },
};
</script>
