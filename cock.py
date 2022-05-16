from edupage_api import Edupage

edupage = Edupage()

try:
    edupage.login("kai.olkowicz", "Kolkowicz12.", "medienberufe.edupage.org")
except BadCredentialsException:
    print("Wrong username or password!")
except LoginDataParsingException:
    print("Try again or open an issue!")