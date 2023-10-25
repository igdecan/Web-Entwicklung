---
title: Data Model
nav_order: 3
---

[Jane Dane]
{: .label }

# [Data model]
{: .no_toc }

<details open markdown="Data-Model">
  <summary>
    Data-Model
  </summary>
  {: .text-delta }

## Benutzerverwaltung:

In erster Linie besteht der Unterschied der Erweiterung darin, dass ich die Benutzerverwaltung integriert habe. Hierbei habe ich eine Klasse ‘User’ erstellt, welche von ‘UserMixin’ erbt und folgende Benutzerinformationen speichert: 
‘id’
‘email’
‘username’
‘password’

Ebenso ist die Klasse ‘User’ mit den Listen und ToDo’s verknüpft, da hier Beziehungen zu ‘ToDo’ und ‘List’ definiert worden sind (Siehe Code; db.py: Zeile 17,18)


## Authentifizierung und Autorisierung:

In der Baseline wurde keine Implementierung für die Authentifizierung und Autorisierung von Benutzern integriert. In der Erweiterung habe ich die Erweiterung ‘Flask-Login’ verwendet, um die Authentifizierung und Autorisierung von Benutzern zu unterstützen. 

Um sicherzustellen, dass die ToDo-Elemente und die Listen mit einem bestimmten Benutzer verknüpft sind, habe ich die ‘user-id’ Spalte zu den ‘Todo’ und ‘List’ Klassen hinzugefügt.

Somit haben nur angemeldete Benutzer die Möglichkeit, To-Do Elemente zu erstellen, anzuzeigen, zu bearbeiten und/oder zu löschen. Hierbei kann jeder Benutzer nur seinen eigenen ToDo Elemente und Listen sehen und bearbeiten. 

## Flask Login

Zur Verwaltung von Benutzersitzungen und die Implementierung Authentifizierungs-Funktionen habe ich die ‘Flask-Login’ Erweiterung verwendet. Dadurch wird den Nutzern die Möglichkeit geboten, sich anzumelden, auszuloggen und ihre Konten zu löschen. 

## Datenbanktabellen und Beziehungen:

Ein weiterer Unterschied besteht in den Datenbanktabellen und Beziehungen. Hier habe ich die Tabellen ‘User’, ‘Todo’ und ‘List’ umstrukturiert, um eine Verknüpfung zwischen Benutzern und ihrer ToDo’s sowie Listen zu ermöglichen und die Benutzerverwaltung zu integrieren.

Die DB enthält drei Haupttabellen: “User”, “Todo” und“List”.
Die Beziehungen der Tabellen werden im folgenden Abschnitt beschrieben.

User:
Die Tabelle "User" dient zur Speicherung von Benutzerinformationen. Dabei wird jeder Benutzer (User) durch eine eindeutige “id” identifiziert. Ebenso werden die E-Mail Adressen “email” und die Benutzernamen “username” der Benutzer (User) in der Tabelle hinterlegt. Um einen Sicherheitsstandard zu gewährleisten, werden die Passwörter “password” gehasht in der Tabelle abgespeichert. 

Es besteht zwischen der “User” Tabelle und der “Todo” sowie “List” Tabellen eine 1-n Beziehung. Das bedeutet, dass ein Benutzer (User) mehrere Aufgaben (Todos) und Listen (List) erstellen bzw. haben kann.

Todo:
Die Tabelle “Todo” enthält die Informationen der Aufgaben, die von Benutzer (User) erstellt werden. Jeder Aufgabe wird eine eindeutige “id” zugewiesen. Die Beschreibungen der Aufgaben werden in der “description” Spalte abgespeichert. Die Spalte “complete” gibt an, ob die Aufgabe abgeschlossen ist oder nicht (True oder False). Die Spalte “user_id” ist eine Fremdschlüsselbeziehung zur Tabelle “Sser” und definiert, zu welchem Benutzer die jeweilige Aufgabe gehört. Es besteht eine n-n Beziehung zwischen der Spalte “lists” und der Tabelle “List”, da eine Aufgabe mehreren Listen zugeordnet werden kann.

List:
Die Tabelle List enthält Informationen über Listen, die von Benutzern erstellt wurden. Jede Liste hat eine eindeutige “id”. Die Spalte “name” enthält den Namen der Liste. Die “user_id” ist eine Fremdschlüsselbeziehung zur Tabelle “User” und gibt an, zu welchem Benutzer (User) die jeweilige Liste gehört. Die Spalte “todos” stellt eine n-n Beziehung zur Tabelle “Todo” dar, da eine Liste mehrere Aufgaben enthalten kann.


## ERD - Entity Realationsship model:

USER
-----
- id (PK)
- email
- username
- password

TODO
-----
- id (PK)
- complete
- description
- user_id (FK to USER)

LIST
-----
- id (PK)
- name
- user_id (FK to USER)

TODO_LIST
----------
- todo_id (FK to TODO, PK)
- list_id (FK to LIST, PK)


- TOC
{:toc}
</details>
