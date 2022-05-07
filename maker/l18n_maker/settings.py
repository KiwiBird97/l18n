import os

LOCALES = ('af', # Afrikaans
        'agq', # Aghem
        'ak', # Akan
        'am', # Amharic
        'ar', # Arabic
        'as', # Assamese
        'asa', # Asu
        'ast', # Asturian
        'az', # Azerbaijani
        'az_Cyrl', # Azerbaijani (Cyrillic)
        'az_Latn', # Azerbaijani (Latin)
        'bas', # Basaa
        'be', # Belarusian
        'bem', # Bemba
        'bez', # Bena
        'bg', # Bulgarian
        'bm', # Bambara
        'bn', # Bangla
        'bo', # Tibetan
        'br', # Breton
        'brx', # Bodo
        'bs', # Bosnian
        'bs_Cyrl', # Bosnian (Cyrillic)
        'bs_Latn', # Bosnian (Latin)
        'ca', # Catalan
        'ccp', # Chakma
        'ce', # Chechen
        'ceb', # Cebuano
        'cgg', # Chiga
        'chr', # Cherokee
        'ckb', # Central Kurdish
        'cs', # Czech
        'cy', # Welsh
        'da', # Danish
        'dav', # Taita
        'de', # German
        'dje', # Zarma
        'doi', # Dogri
        'dsb', # Lower Sorbian
        'dua', # Duala
        'dyo', # Jola-Fonyi
        'dz', # Dzongkha
        'ebu', # Embu
        'ee', # Ewe
        'el', # Greek
        'en', # English
        'eo', # Esperanto
        'es', # Spanish
        'et', # Estonian
        'eu', # Basque
        'ewo', # Ewondo
        'fa', # Persian
        'ff', # Fulah
        'ff_Adlm', # Fulah (Adlam)
        'ff_Latn', # Fulah (Latin)
        'fi', # Finnish
        'fil', # Filipino
        'fo', # Faroese
        'fr', # French
        'fur', # Friulian
        'fy', # Western Frisian
        'ga', # Irish
        'gd', # Scottish Gaelic
        'gl', # Galician
        'gsw', # Swiss German
        'gu', # Gujarati
        'guz', # Gusii
        'gv', # Manx
        'ha', # Hausa
        'haw', # Hawaiian
        'he', # Hebrew
        'hi', # Hindi
        'hr', # Croatian
        'hsb', # Upper Sorbian
        'hu', # Hungarian
        'hy', # Armenian
        'ia', # Interlingua
        'id', # Indonesian
        'ig', # Igbo
        'ii', # Sichuan Yi
        'is', # Icelandic
        'it', # Italian
        'ja', # Japanese
        'jgo', # Ngomba
        'jmc', # Machame
        'jv', # Javanese
        'ka', # Georgian
        'kab', # Kabyle
        'kam', # Kamba
        'kde', # Makonde
        'kea', # Kabuverdianu
        'khq', # Koyra Chiini
        'ki', # Kikuyu
        'kk', # Kazakh
        'kkj', # Kako
        'kl', # Kalaallisut
        'kln', # Kalenjin
        'km', # Khmer
        'kn', # Kannada
        'ko', # Korean
        'kok', # Konkani
        'ks', # Kashmiri
        'ks_Arab', # Kashmiri (Arabic)
        'ksb', # Shambala
        'ksf', # Bafia
        'ksh', # Colognian
        'ku', # Kurdish
        'kw', # Cornish
        'ky', # Kyrgyz
        'lag', # Langi
        'lb', # Luxembourgish
        'lg', # Ganda
        'lkt', # Lakota
        'ln', # Lingala
        'lo', # Lao
        'lrc', # Northern Luri
        'lt', # Lithuanian
        'lu', # Luba-Katanga
        'luo', # Luo
        'luy', # Luyia
        'lv', # Latvian
        'mai', # Maithili
        'mas', # Masai
        'mer', # Meru
        'mfe', # Morisyen
        'mg', # Malagasy
        'mgh', # Makhuwa-Meetto
        'mgo', # Metaʼ
        'mi', # Māori
        'mk', # Macedonian
        'ml', # Malayalam
        'mn', # Mongolian
        'mni', # Manipuri
        'mni_Beng', # Manipuri (Bangla)
        'mr', # Marathi
        'ms', # Malay
        'mt', # Maltese
        'mua', # Mundang
        'my', # Burmese
        'mzn', # Mazanderani
        'naq', # Nama
        'nb', # Norwegian Bokmål
        'nd', # North Ndebele
        'ne', # Nepali
        'nl', # Dutch
        'nmg', # Kwasio
        'nn', # Norwegian Nynorsk
        'nnh', # Ngiemboon
        'no', # Norwegian
        'nus', # Nuer
        'nyn', # Nyankole
        'om', # Oromo
        'or', # Odia
        'os', # Ossetic
        'pa', # Punjabi
        'pa_Arab', # Punjabi (Arabic)
        'pa_Guru', # Punjabi (Gurmukhi)
        'pcm', # Nigerian Pidgin
        'pl', # Polish
        'ps', # Pashto
        'pt', # Portuguese
        'qu', # Quechua
        'rm', # Romansh
        'rn', # Rundi
        'ro', # Romanian
        'rof', # Rombo
        'ru', # Russian
        'rw', # Kinyarwanda
        'rwk', # Rwa
        'sa', # Sanskrit
        'sah', # Sakha
        'saq', # Samburu
        'sat', # Santali
        'sbp', # Sangu
        'sc', # Sardinian
        'sd', # Sindhi
        'sd_Arab', # Sindhi (Arabic)
        'sd_Deva', # Sindhi (Devanagari)
        'se', # Northern Sami
        'seh', # Sena
        'ses', # Koyraboro Senni
        'sg', # Sango
        'shi', # Tachelhit
        'shi_Latn', # Tachelhit (Latin)
        'shi_Tfng', # Tachelhit (Tifinagh)
        'si', # Sinhala
        'sk', # Slovak
        'sl', # Slovenian
        'smn', # Inari Sami
        'sn', # Shona
        'so', # Somali
        'sq', # Albanian
        'sr', # Serbian
        'sr_Cyrl', # Serbian (Cyrillic)
        'sr_Latn', # Serbian (Latin)
        'su', # Sundanese
        'su_Latn', # Sundanese (Latin)
        'sv', # Swedish
        'sw', # Swahili
        'ta', # Tamil
        'te', # Telugu
        'teo', # Teso
        'tg', # Tajik
        'th', # Thai
        'ti', # Tigrinya
        'tk', # Turkmen
        'to', # Tongan
        'tr', # Turkish
        'tt', # Tatar
        'twq', # Tasawaq
        'tzm', # Central Atlas Tamazight
        'ug', # Uyghur
        'uk', # Ukrainian
        'ur', # Urdu
        'uz', # Uzbek
        'uz_Arab', # Uzbek (Arabic)
        'uz_Cyrl', # Uzbek (Cyrillic)
        'uz_Latn', # Uzbek (Latin)
        'vai', # Vai
        'vai_Latn', # Vai (Latin)
        'vai_Vaii', # Vai (Vai)
        'vi', # Vietnamese
        'vun', # Vunjo
        'wae', # Walser
        'wo', # Wolof
        'xh', # Xhosa
        'xog', # Soga
        'yav', # Yangben
        'yi', # Yiddish
        'yo', # Yoruba
        'yue', # Cantonese
        'yue_Hans', # Cantonese (Simplified)
        'yue_Hant', # Cantonese (Traditional)
        'zgh', # Standard Moroccan Tamazight
        'zh', # Chinese
        'zh_Hans', # Chinese (Simplified)
        'zh_Hant', # Chinese (Traditional)
        'zu', # Zulu
)
CLDR_DATA_URL = 'http://www.unicode.org/Public/cldr/latest'

LOCALE_PATH = os.path.join(
    os.sep.join(os.path.dirname(__file__).split(os.sep)[:-2]),
    'l18n', 'locale'
)

PO_PATH = os.path.join(LOCALE_PATH, '%s', 'LC_MESSAGES', 'l18n.po')

PY_PATH = os.path.join(
    os.sep.join(os.path.dirname(__file__).split(os.sep)[:-2]),
    'l18n', '__maps.py'
)
