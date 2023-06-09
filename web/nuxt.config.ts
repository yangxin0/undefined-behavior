// https://nuxt.com/docs/api/configuration/nuxt-config
const appName = process.env.NUXT_PUBLIC_APP_NAME ?? 'GPT Pro'

export default defineNuxtConfig({
    debug: process.env.NODE_ENV !== 'production',
    ssr: true,
    app: {
        head: {
            title: appName,
        },
    },
    runtimeConfig: {
        public: {
            appName: appName,
            typewriter: true,
            typewriterDelay: 50,
            customApiKey: false
        }
    },
    build: {
        transpile: ['vuetify']
    },
    css: [
        'vuetify/styles',
        'material-design-icons-iconfont/dist/material-design-icons.css',
        'highlight.js/styles/panda-syntax-dark.css',
    ],
    modules: [
        '@kevinmarrec/nuxt-pwa',
        '@nuxtjs/color-mode',
        '@nuxtjs/i18n'
    ],
    pwa: {
        manifest: {
            name: appName,
            short_name: appName,
            description: 'A ChatGPT web Client'
        },
        workbox: {
            enabled: process.env.DEBUT_PWA === 'true',
        }
    },
    i18n: {
        strategy: 'no_prefix',
        locales: [
            {
                code: 'en',
                iso: 'en-US',
                name: 'English',
                file: 'en-US.json',
            },
            {
                code: 'zh-CN',
                iso: 'zh-CN',
                name: '简体中文',
                file: 'zh-CN.json',
            }
        ],
        lazy: true,
        langDir: 'lang',
        defaultLocale: 'en',
        vueI18n: {
            fallbackLocale: 'en',
        },
    }
})
