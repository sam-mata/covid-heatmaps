// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ['@nuxt/ui', "@samk-dev/nuxt-vcalendar", "@nuxt/fonts", "@nuxtjs/tailwindcss"],
  devtools: { enabled: true },

  routeRules: {
    // prerender index route by default
    '/': { prerender: true },
  },
   runtimeConfig: {
    public: {
      MAPBOX: process.env.MAPBOX
    }
  }

});