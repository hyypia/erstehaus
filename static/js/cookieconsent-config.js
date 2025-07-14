import "https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@3.1.0/dist/cookieconsent.umd.js";

CookieConsent.run({
  categories: {
    necessary: {
      enabled: true, // this category is enabled by default
      readOnly: true, // this category cannot be disabled
    },
    analytics: {},
    maps: {},
  },
  language: {
    default: "de",
    translations: {
      de: {
        consentModal: {
          title: "Diese Website verwendet Cookies",
          description:
            "Wir verwenden Cookies, um unsere Website nutzerfreundlicher zu gestalten und Inhalte von Drittanbietern (z. B. Google Maps) einzubinden. Einige Cookies sind für den Betrieb der Seite notwendig, andere dienen anonymen Statistikzwecken. Sie können selbst entscheiden, welche Kategorien Sie zulassen möchten.",
          acceptAllBtn: "Alle akzeptieren",
          acceptNecessaryBtn: "Alle ablehnen",
          showPreferencesBtn: "Einstellungen",
        },
        preferencesModal: {
          title: "Einstellungen",
          acceptAllBtn: "Alle akzeptieren",
          acceptNecessaryBtn: "Alle ablehnen",
          savePreferencesBtn: "Speichern",
          closeIconLabel: "Close modal",
          sections: [
            {
              description:
                "Wir nutzen Cookies auf unserer Website. Einige von ihnen sind technisch notwendig, um unsere Website darzustellen. Andere helfen uns, die Website stetig zu verbessern. Auf unserer Webseite setzen wir folgende Cookies:",
            },
            {
              title: "technisch notwendige Cookies",
              description:
                "Technisch notwendige Cookies gewährleisten wesentliche Funktionen der Website. Sie speichern keine persönlich identifizierbaren Informationen.",

              //this field will generate a toggle linked to the 'necessary' category
              linkedCategory: "necessary",
            },
            {
              title: "Statistik",
              description:
                "Statistik-Cookies helfen uns, Nutzerinformationen über deren Website-Besuch anonym zu sammeln, um das Online-Angebot bedarfsgerecht ausrichten zu können.",
              linkedCategory: "analytics",
            },
            {
              title: "Google Maps",
              description:
                "Google Maps ist eine Internet-Kartenplattform, die detaillierte geografische Informationen liefert. Wenn Sie diesem Dienst einwilligen, werden Inhalte von dieser Plattform auf dieser Website angezeigt.",
              linkedCategory: "maps",
            },
            {
              title: "Datenschutzerklärung",
              description:
                'Weitere Informationen finden Sie in unserer <a href="#contact-page">Datenschutzerklärung</a>',
            },
          ],
        },
      },
    },
  },
  guiOptions: {
    consentModal: {
      layout: "cloud wide",
      position: "bottom center",
      flipButtons: true,
    },
  },
});
