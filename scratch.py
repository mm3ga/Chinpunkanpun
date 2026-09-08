import argostranslate.package
import argostranslate.translate
from requests import packages

from_code = "ja"
to_code = "en"
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

print(type(available_packages))
print(len(available_packages))

#for number, package in enumerate(available_packages):
    #if package.from_code == "ja" and package.to_code == "en":
        #download_path = package.download()
        #argostranslate.package.install_from_path(download_path)

test_text = "僕はを日本語勉強していましたでも美味しい"

resultor = argostranslate.translate.translate(
    test_text,
    "ja",
    "en",
)

print(resultor)
