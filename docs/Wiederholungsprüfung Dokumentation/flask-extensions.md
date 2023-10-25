---
title: Flask Extensions
nav_order: 2
---

[Jane Dane]
{: .label }

# [Flask-Extensions]
{: .no_toc }

<details open markdown="Flask-Login">
  <summary>
    Flask-Login
  </summary>
  {: .text-delta }

## Flask-Login

Die Implementierung der Benutzerauthentifizierung und der Sessions in der Webanwendung mittels Flask-Login gestaltete sich aufgrund der umfangreichen und einfachen Dokumentation einfach. So konnte ich die Webanwendung anhand der Dokumentation erweitern und anpassen. Diese Funktionalität ist entscheidend für die reibungslose Umsetzung der Login- und Logout-Prozesse. Ebenso einfach lässt sich Flask-Login in den Code integrieren. Zusätzlich bietet Flask-Login eine einfache Verwaltung von Benutzersitzungen. 

Der gesamte Authentifizierungsprozess inklusive Anmelde-, Abmelde-, Registrierungs-, Passwortänderungs- und Konto-Löschfunktionen werden jedoch nicht von Flask-Login übernommen.Dieser Teil wurde von mir individuell in den Code implementiert. Dies ermöglicht es mir, die Kontrolle über diese Funktionen zu behalten. So kann ich sicherstellen, dass diese den spezifischen Anforderungen des Projekts entsprechen. 

Im Folgenden gehe ich auf die Punkte ein, wie Flask-Login und der Code zusammenarbeiten. 

Flask-Login kümmert sich um die Verwaltung der Benutzersitzungen. Wenn sich ein Benutzer (User) erfolgreich anmeldet, wird für ihn eine Session gestartet und seine Informationen werden in der Session gespeichert. Dadurch können Benutzer (User) nach der Anmeldung identifiziert und personalisierte Funktionen zur Verfügung gestellt werden.  

Diese An- und Abmeldefunktionen befinden sich in der Datei “auth.py”. Sie werden beim An-/Abmelden aufgerufen. 
In der Anmeldemethode wird die Email-Adresse sowie das Passwort überprüft. Sind die persönlichen Anmeldeinformationen korrekt, wird der Benutzer (User) mittels “login_user(user)” durch Flask-Login als angemeldet markiert.
In der Abmeldemethode wird der Benutzer wiederum mit “logoutuser()” von Flask-Login als abgemeldet markiert.

Die Registrierungsfunktion ist ebenso in der Datei “auth.py”. Hier wird überprüft, ob der Benutzer bereits existiert und ob die eingegebenen Daten gültig sind. Flask-Login spielt eine Schlüsselrolle, da hier ebenso die Benutzersitzung und Authentifizierung in Ihrer Anwendung verwaltet wird. 

Bei der Passwortänderung sowie Kontolöschung stellt Flask-Login sicher, dass diese Funktionen nur für den jeweiligen angemeldeten Benutzer (User) zur Verfügung stehen und die Änderungen nur in diesen Konten vorgenommen werden.

Wenn sich ein Benutzer anmeldet, werden sowohl die von Flask-Login erstellten Sessions als auch die benutzerdefinierten Anmeldefunktionen sowie Benutzer Verwaltungsfunktionen verwendet. Dabei übernimmt Flask-Login die Verwaltung der Sessions, während mein Code die Überprüfung der Anmeldung, Abmeldung, Registrierung, Löschung, Änderun und das Setzen des Benutzers als angemeldet übernimmt.

- TOC
{:toc}
</details>




<details open markdown="block">
  <summary>
    RESTful API
  </summary>
  {: .text-delta }


In meiner Erweiterung habe ich Flask-RESTful verwendet, um die Implementierung einer RESTful API in der Anwendung zu erleichtern und damit auch die Wartbarkeit der API zu unterstützen. Die Erweiterung bietet eine klare und konsistente Methode, um API-Endpunkte zu erstellen, Anfragen zu verarbeiten und Daten zu validieren. 

Einfachheit, Verständlichkeit und eine saubere Art, API Ressourcen und Endpunkte zu definieren, waren wichtig. Ebenso verfügt Flask-RESTful über eine einfache und umfassende Dokumentation, die mir geholfen hat, die Erweiterung effektiv zu nutzen.

In erster Linie habe ich die Flask-RESTful Erweiterung in das Projekt integriert, siehe “requierments.tx”t. Im Code werden die verschiedenen Endpunkte der API durch erstellte Ressourcenklassen repräsentiert. Um die Funktionalität im Zusammenhang mit den ToDo Elementen zu behandeln, wurden zwei Hauptklassen erstellt, “AllTodos” und “SpecificTodo”.

“AllTodos”: Diese Klasse wird verwendet, um Anfragen zum Abrufen aller ToDo-Elemente zu behandeln. Um die ToDo-Elemente aus der Datenbank zu holen und als JSON-Daten zurückzugeben, wurde hier die Methode “get” implementiert.

“SpecificTodo” implementiert: Die Klasse behandelt Anfragen, die sich auf ein spezifisches ToDo beziehen.  Um das Abrufen, Anlegen, Aktualisieren und Löschen zu ermöglichen, wurden die Methoden “get”, “post”, “patch” und “delete” implementiert.

Hierbei wird das Marshalling Verfahren verwendet. Dadurch werden die Daten, die von der API zurückgegeben werden, in das gewünschte JSON-Format konvertiert. 

## Anfragemethoden

“get”: Diese Methode wird verwendet, um Daten abzurufen. Mit “AllTodos” werden alle ToDo-Elemente abgerufen, während mit “SpecificTodo” nur ein einzelnes ToDo-Element auf Basis der jeweiligen ID abgerufen wird. 

“post”: Mit dieser Methode können neue ToDo-Elemente erstellt werden. Übermittelte Daten werden validiert und der Datenbank hinzugefügt.

“patch”: Mit dieser Methode können bestehende ToDo-Elemente aktualisiert werden. 

“löschen”: Mit dieser Methode können ToDo-Elemente anhand ihrer ID gelöscht werden.







- TOC
{:toc}
</details>
