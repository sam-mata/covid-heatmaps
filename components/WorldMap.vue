<template>
  <div ref="mapContainer" class="w-full h-full"></div>
</template>

<script>
import mapboxgl from 'mapbox-gl';
import data from '../data.js';

export default {
  mounted() {
    mapboxgl.accessToken = 'pk.eyJ1IjoibWF0YXNhbXUiLCJhIjoiY2x4MnRzOGJqMG1kYTJub21tM3YzZWMyeCJ9.gWwXsEB5lyc3KgDHYYhGLg';
    const map = new mapboxgl.Map({
      container: this.$refs.mapContainer,
      // style: 'mapbox://styles/matasamu/clxdxx2b0000s01rn8v4f87gg',
      style: 'mapbox://styles/mapbox/light-v10',
      center: [0, 0],
      zoom: 2,
      interactive: true,
    });

    map.on('load', () => {
      map.addSource('countries', {
        type: 'geojson',
        data: data,
      });

      map.addLayer({
        id: 'choropleth',
        type: 'fill',
        source: 'countries',
        paint: {
          'fill-color': [
            'interpolate',
            ['linear'],
            ['get', 'total_cases'],
            0,
            '#F2F12D',
            100,
            '#EED322',
            1000,
            '#E6B71E',
            10000,
            '#DA9C20',
            100000,
            '#CA8323',
            1000000,
            '#B86B25',
            100000000,
            '#A25626',
          ],
          'fill-opacity': 0.2,
        },
      });
    });
  },
};
</script>