from django.urls import path, include


urlpatterns = [
    path('', include('accounts.api.v1.urls.accounts')),
    path('profile/', include('accounts.api.v1.urls.profiles')),
]


# vaghti tedad urls hamon mire bala mitonim yek folder be esme urls bezanim
# va dakhel on file haye moutaafaveti be esme url haei ke darim besazim va url haye marbot be har file ro onja gharar bedim

# example:   masalan ma dakhel file urls app accounts 10 ta url darim ke 6 tash baraye register, rest-pass, login, logout va ... hast
# va 4 tash baraye urls haye digas ke marbot be on 6 ta nist.
# miyaim yek folder be esme urls dakhel on app misazim va dakhel on file haei be esme
# accounts.py va other.py misazim va dakhel on url haye marbote ro gharar midim baraye inke django betone on url haro beshnase
# baiad __init__.py besazim va dakhelsh on 2 ta file ro include konim
