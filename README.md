1. Opis aplikacije
Beauty Shelf je web aplikacija dizajnirana kao digitalni ormarić za kozmetiku. Služi korisnicima
da prate rok trajanja svojih proizvoda nakon otvaranja (PAO - Period After Opening). Korisnik
unosi brend, tip proizvoda i datum otvaranja, a aplikacija automatski izračunava datum isteka,
čuva ga u bazi i vizuelno upozorava (zelenom, žutom ili crvenom bojom) na status proizvoda.

Tehnologije koje se koriste:
• Frontend: HTML5, CSS3, JavaScript (Vanilla JS)
• Backend: Python Flask sa Flask-CORS
• Baza podataka: PostgreSQL
• Kontejnerizacija: Docker i Docker Compose
• Orkestracija: Docker Compose


2. Link repozitorija
   
GitHub repozitorij: git@github.com:MarinelaMitic/beauty-app.git


3. Softverski preduslovi
   
Za pokretanje aplikacije potrebni su sljedeći softver i verzije:
• Docker Desktop: verzija 4.0 ili novija
• Docker Compose: verzija 2.0 ili novija (uključen u Docker Desktop)
• Operativni sistem: macOS, Linux ili Windows (sa WSL2)
• Pretraživač: Bilo koji moderan pretraživač (Chrome, Firefox, Safari, Edge)
• Terminal/CLI: Bash ili Zsh


4. Arhitektura aplikacije
   
Aplikacija koristi mikroservisnu arhitekturu sa tri osnovne komponente:
1. Klijentski sloj (Frontend): Nginx kontejner koji servira statički sadržaj.
2. Logički sloj (Backend): Flask API koji obrađuje kalkulacije i komunikaciju s bazom.
3. Sloj podataka (Database): PostgreSQL kontejner za trajno čuvanje podataka.
Svi servisi su povezani u zajedničku internu Docker mrežu pod nazivom beauty_network.


5. Opis servisa, mreža i volumena
   
Servisi:
• beauty_frontend: Radi na portu 80 (mapiran na 8080 hosta). Koristi zvanični
nginx:alpine image.
• beauty_backend: Python aplikacija na portu 5000. Podržava hot-reload preko
montiranog volumena.
• beauty_db: PostgreSQL 15 baza podataka.
Mreža: beauty_network (bridge driver) omogućava izolovanu i sigurnu komunikaciju između
servisa.

Volumeni:
• beauty_data: Trajna pohrana (persistence) za PostgreSQL podatke u /var/lib/
postgresql/data.
• Lokalni mount: Za backend kod radi lakšeg razvoja i testiranja.


6. Upute za pokretanje
   
Aplikacija se pokreće u nekoliko koraka:
1. Klonirajte repozitorij i uđite u root folder projekta.
2. Kreirajte .env fajl sa potrebnim varijablama (DB_USER, DB_PASSWORD...).
3. Dodijelite permisije skriptama: chmod +x *.sh.
4. Pokrenite pripremu: ./pripremi_aplikaciju.sh.
5. Pokrenite aplikaciju: ./pokreni_aplikaciju.sh.

   
7. Način pristupa aplikaciji
   
Nakon pokretanja, aplikaciji možete pristupiti putem browsera na:
• URL: http://localhost:8080
• API (Backend): http://localhost:5000


8. Korištenje AI alata

Korišteni alat: Google Gemini (Gemini 1.5 Flash model).

Pregled promptova i intervencija:
1. Prompt: "Želim napraviti 'Beauty Shelf' aplikaciju za praćenje rokova šminke. Predloži
mi modernu paletu pink boja i CSS stil za dugmad."
◦ Šta je prihvaćeno: HEX kodovi boja i linear-gradient za glavno dugme.
◦ Šta je izmijenjeno: Ručno sam podesila box-shadow i zaobljene rubove da
aplikacija izgleda nježnije.

2. Prompt: "Daj mi listu od 20-30 poznatih kozmetičkih brendova i razvrstaj ih na
drogerijske i luksuzne."
◦ Šta je prihvaćeno: Nazivi brendova.
◦ Šta je izmijenjeno: Sama sam kreirala strukturu u HTML-u koristeći
<optgroup> i dodala brendove poput Aure i Kiko Milana.
  
3. Prompt: "Kako u Pythonu pomoću datetime modula izračunati datum koji je tačno 6 ili
12 mjeseci nakon otvaranja?"
◦ Šta je prihvaćeno: Logika dodavanja mjeseci preko timedelta.
◦ Šta je izmijenjeno: Prilagodila sam funkciju da podatke prima direktno iz forme i
formatirala ispis na evropski način.
  
4. Prompt: "Napiši JS logiku koja će u tabeli obojiti cijeli red u narandžasto ako je do
isteka proizvoda ostalo manje od 10 dana."
◦ Šta je prihvaćeno: Logički uslov if (dana_do <= 10).
◦ Šta je izmijenjeno: Kreirala sam specifičnu CSS klasu warning-row koja se
estetski slaže uz temu.
  
5. Prompt: "Zašto mi se cijela forma pomjerila u stranu kad sam dodala labelu, a stavila
sam margin: 0 auto;?"
◦ Šta je prihvaćeno: Objašnjenje o display: block i širini elementa.
◦ Šta je izmijenjeno: Ručno sam podesila width: 90% i poravnanje labela iznad
polja.
  
6. Prompt: "Kako napraviti da se polja u formi zacrvene ako korisnik zaboravi unijeti
brend ili datum?"
◦ Šta je prihvaćeno: JS funkcija koja dodaje is-invalid klasu.
◦ Šta je izmijenjeno: Dodala sam shake animaciju polja i poruku upozorenja na
bosanskom jeziku.
  
7. Prompt: "Kako u JavaScriptu očistiti listu proizvoda i napuniti je novim stavkama kada
korisnik promijeni kategoriju?"
◦ Šta je prihvaćeno: Metoda innerHTML = '' za resetovanje liste.
◦ Šta je izmijenjeno: Sama sam sastavila sve nizove proizvoda na našem jeziku i
povezala ih sa kategorijama.
  
8. Prompt: "Input polja mi izgledaju super, ali select liste su mi šire od njih i izlaze van
forme. Kako da to popravim?"
◦ Šta je prihvaćeno: Savjet o korištenju box-sizing: border-box;.
◦ Šta je izmijenjeno: Primijenila sam pravilo na sve elemente i ujednačila padding
na 14px.
  
9. Prompt: "Koje su standardne environment varijable (DB_USER, DB_PASS) potrebne da
se Flask poveže sa Postgresom u Dockeru?"
◦ Šta je prihvaćeno: Nazivi varijabli za .env fajl.
◦ Šta je izmijenjeno: Samostalno sam kreirala .env fajl sa unikatnim lozinkama i
mapirala ih u Compose.
  
10. Prompt: "Kako u docker-compose.yml podesiti volumen za Postgres bazu da moji
uneseni proizvodi ne nestanu?"
◦ Šta je prihvaćeno: Sintaksa za volumes unutar servisa baze.
◦ Šta je izmijenjeno: Ručno sam kreirala volumen beauty_data i povezala ga na
ispravnu putanju baze.
  
11. Prompt: "Objasni mi razliku između ports i EXPOSE u Dockeru, želim da aplikacija
radi na portu 8080."
◦ Šta je prihvaćeno: Objašnjenje mapiranja portova hosta i kontejnera.
◦ Šta je izmijenjeno: Na osnovu toga sam samostalno napisala Dockerfile-ove i
konfigurisala Nginx.
