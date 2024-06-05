<template>
    <div ref="mapContainer" class="map-container"></div>
</template>

<script>
export default {
    mounted() {
        if (process.client) {
            this.initMap();
        }
    },
    methods: {
        initMap() {
            import('leaflet').then((L) => {
                import('leaflet/dist/leaflet.css');
                import('../data/countries-110m.json').then((worldData) => {
                    const map = L.map(this.$refs.mapContainer).setView([0, 0], 2);

                    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                    }).addTo(map);

                    const geojsonLayer = L.geoJSON(worldData, {
                        style: {
                            fillColor: 'black',
                            weight: 1,
                            opacity: 1,
                            color: 'gray',
                            fillOpacity: 1,
                        },
                        onEachFeature: (feature, layer) => {
                            layer.on({
                                mouseover: this.highlightFeature,
                                mouseout: this.resetHighlight,
                            });
                        },
                    }).addTo(map);

                    map.fitBounds(geojsonLayer.getBounds());
                });
            });
        },
        highlightFeature(e) {
            const layer = e.target;
            layer.setStyle({
                fillColor: 'blue',
            });
        },
        resetHighlight(e) {
            const layer = e.target;
            layer.setStyle({
                fillColor: 'white',
            });
        },
    },
};
</script>

<style scoped>
.map-container {
    width: 100%;
    height: 100%;
}
</style>