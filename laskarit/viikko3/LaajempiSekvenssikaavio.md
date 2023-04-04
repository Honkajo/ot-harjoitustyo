```mermaid
sequenceDiagram
    participant main
    participant laitehallinto
    participant rautatietori
    participant ratikka6
    participant bussi244
    participant lippu_luukku
    participant kallen_kortti
    main->>laitehallinto: create HKLLaitehallinto object
    main->>rautatietori: create Lataajalaite object
    main->>ratikka6: create Lukijalaite object
    main->>bussi244: create Lukijalaite object
    laitehallinto->>rautatietori: lisaa_lataaja(rautatietori)
    laitehallinto->>ratikka6: lisaa_lukija(ratikka6)
    laitehallinto->>bussi244: lisaa_lukija(bussi244)
    main->>lippu_luukku: create Kioski object
    lippu_luukku->>kallen_kortti: osta_matkakortti("Kalle", None)
    rautatietori->>kallen_kortti: osta_lippu(kallen_kortti, 0)
    bussi244->>kallen_kortti: osta_lippu(kallen_kortti, 2)
