// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxt/ui',
    "@samk-dev/nuxt-vcalendar",
    "@nuxt/fonts",
    "@nuxtjs/tailwindcss",
    "nuxt3-leaflet"
  ],
  devtools: { enabled: true },

  routeRules: {
    // prerender index route by default
    '/': { prerender: true },
  },

});
