---
title: Value Proposition
nav_order: 1
---

[Jane Dane]
{: .label }

# [Value proposition]
{: .no_toc }

<details open markdown="Persona">
  <summary>
  Persona 
  </summary>
  {: .text-delta }

## Persona: Lisa

- **Name:** Lisa
- **Alter:** 26
- **Beruf:** Projektmanagerin
- **Bedürfnisse:** Effizientes Aufgabenmanagement, Zusammenarbeit im Team, Zeitersparnis
- **Schmerzpunkte:** Unorganisierte Aufgaben, zeitraubende Kommunikation

- TOC
{:toc}
</details>

<details open markdown="Value Proposition">
  <summary>
  Value Proposition
  </summary>
  {: .text-delta }

## Funktionen der Webanwendung

Im Folgenden werden die Funktionen der Erweiterung der Web-Anwendung in Bezug auf die Persona beschrieben.

### Lisa, 26 Jahre, Projektmanagerin

Lisa, 26 Jahre, ist Projektmanagerin und arbeitet erfolgreich in einem Unternehmen, jedoch sind ihre Aufgaben unorganisiert. Dies wiederum kostet ihr sehr viel Zeit, wodurch Lisa sich nach einem Tool sucht, um dieses Problem zu lösen.

### Login/Registrierung

Lisas Aufgaben sind streng geheim. Aus diesem Grund ist es wichtig, dass sie sich in ihren eigenen Account mit Benutzername/Email und Passwort einloggen kann. Um das Entschlüsseln des Passwortes nicht zu einfach zu machen, wird das Passwort gehasht, bevor es in der Datenbank gespeichert wird. Um sicherzugehen, dass Lisa bei der Passwortgenerierung das Passwort richtig eingibt, wird eine Doppelkontrolle durchgeführt. Sobald die beiden Passwörter nicht übereinstimmen, wird der Vorgang abgebrochen und eine Meldung ausgegeben, dass die Passwörter nicht übereinstimmen.

- Login -> Eingabe der Anmeldeinformationen -> Login
- Signup -> Eingabe aller Informationen -> Sign Up

### Passwortänderung

Um die Sicherheit ihres Kontos zu gewährleisten, möchte Lisa ihr Passwort alle zwei Monate ändern. Lisa hat die Möglichkeit, ihr Passwort in der Web-Anwendung zu ändern.

- Einloggen -> Profile -> Password Change

### Löschung des Accounts

Wenn Lisa sich entscheidet, diese Webanwendung nicht als Tool zu nutzen, hat sie die Möglichkeit, über "Login -> Profile -> Delete Account" ihren Account und damit ihre Daten zu löschen.

### Erstellung eines To-Do’s

Lisa kann ein "Todo" erstellen, indem sie die gewünschte Beschreibung in das Eingabefeld eingibt und auf "Create" klickt.

- Todos -> Eingabe der Information -> Create

### Bearbeiten eines To-Do’s

Lisa hat die Möglichkeit, ein ToDo durch Anklicken zu bearbeiten, einer Liste zuzuweisen oder zu löschen.

- Todos -> Klicken auf ein Todo -> Update Todo / Delete Todo

### Erstellen einer Liste

Lisa kann beliebige Listen erstellen, um ihre Arbeit strukturiert zu erledigen. Mit "Lists -> Eingabe der Information -> Create" kann Lisa eine Liste erstellen.


- TOC
{:toc}
</details>

