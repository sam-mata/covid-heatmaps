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
            0, 'hsl(100, 100%, 50%)',
            1000, 'hsl(90, 100%, 50%)',
            10000, 'hsl(90, 100%, 50%)',
            100000, 'hsl(80, 100%, 50%)',
            500000, 'hsl(70, 100%, 50%)',
            750000, 'hsl(60, 100%, 50%)',
            1000000, 'hsl(50, 100%, 50%)',
            5000000, 'hsl(40, 100%, 50%)',
            10000000, 'hsl(30, 100%, 50%)',
            50000000, 'hsl(20, 100%, 50%)',
            500000000, 'hsl(10, 100%, 50%)',
          ],
          'fill-opacity': 0.2,
        },
      });
    });
  },
};
</script>