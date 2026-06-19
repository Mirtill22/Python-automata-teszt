# Python-automata-teszt
A test.py program a https://automationteststore.com/ oldalon lévő vásárlást teszteli le a test_shirt_purchase() függvénnyel

- Beállítja a böngészőt, a kezdő oldalt, és elindítja a tracing folyamatot
- A felső menüben rákattint az "Account" feliratra, az azt követő oldalon pedig az új felhasználó regisztrálása folyamatot indítja el a "Continue" gomb megnyomásával
- Kitölti a mezőket (név, e-mail cím, stb.) teszt adatokkal, majd megad egy teszt felhasználó nevet és jelszót
- A hírlevelekre nem iratkozik fel, elfogadja az ÁSZF-t, és a "Continue" gomb megnyomásával regisztrál egy új felhasználót.
- A kategóriáknál kiválasztja az "Apparel & accessories"-t, azon belül a pólókat, azokat ár szerint csökkenő sorrendbe helyezi, majd a legdrágábbat kosárba helyezi, onnan pedig a "Continue shopping" gombbal visszatér a vásárláshoz
- A folyamatot megismétli, ebben az esetben a 2. készleten lévő legdrágább pólóval, a kosárból itt viszont a "Checkout" gombra kattintva elindítja a megrendelést, az összesítő oldalon a "Confirm order" gombot megnyomva pedig véglegesíti azt
- Az végső oldal a rendelés sikerességének visszaigazolása, ezt leellenőrzi
- A tracinget lementi a test-results mappába zip formátumban, a böngészőt bezárja.
