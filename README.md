# ip no create

documentation brève du projet.

---

## Table des Matières

1. [Utilisateur](#1-utilisateur)
    - [Enregistrement](#enregistrement)
    - [Obtention des jetons](#obtention-des-jetons)
    - [Rafraîchissement du jeton](#rafraîchissement-du-jeton)
2. [Tableau (Board)](#2-tableau-board)
    - [Tous les tableaux](#tous-les-tableaux)
    - [Nouveau tableau](#nouveau-tableau)
    - [Détails du tableau](#détails-du-tableau)
    - [Mise à jour du tableau](#mise-à-jour-du-tableau)
    - [Suppression du tableau](#suppression-du-tableau)
    - [Ajout d'utilisateur au tableau](#ajout-dutilisateur-au-tableau)
    - [Suppression d'utilisateur du tableau](#suppression-dutilisateur-du-tableau)
3. [Liste (List)](#3-liste-list)
    - [Toutes les listes pour un tableau](#toutes-les-listes-pour-un-tableau)
    - [Nouvelle liste pour un tableau](#nouvelle-liste-pour-un-tableau)
    - [Détails de la liste](#détails-de-la-liste)
    - [Mise à jour de la liste](#mise-à-jour-de-la-liste)
    - [Suppression de la liste](#suppression-de-la-liste)
4. [Carte (Card)](#4-carte-card)
    - [Toutes les cartes pour une liste](#toutes-les-cartes-pour-une-liste)
    - [Nouvelle carte pour une liste](#nouvelle-carte-pour-une-liste)
    - [Détails de la carte](#détails-de-la-carte)
    - [Mise à jour de la carte](#mise-à-jour-de-la-carte)
    - [Suppression de la carte](#suppression-de-la-carte)

---

## 1. Utilisateur

### Enregistrement

- **Méthode :** POST
- **Endpoint :** `/register/`
- **Description :** Enregistre un nouvel utilisateur.
- **Corps de la requête :**
  - `username` : Nom d'utilisateur
  - `password` : Mot de passe de l'utilisateur
- **Permissions :** Aucune
- **Réponse :**
  - Statut 200 OK : Enregistrement réussi
  - Statut 400 BAD REQUEST : Entrée invalide ou échec de l'enregistrement

### Obtention des jetons

- **Méthode :** POST
- **Endpoint :** `/token/`
- **Description :** Obtient une paire de jetons d'accès et de rafraîchissement.
- **Corps de la requête :**
  - `username` : Nom d'utilisateur
  - `password` : Mot de passe de l'utilisateur
- **Permissions :** Aucune
- **Réponse :**
  - Statut 200 OK : Jetons obtenus avec succès
  - Statut 401 UNAUTHORIZED : Authentification échouée

### Rafraîchissement du jeton

- **Méthode :** POST
- **Endpoint :** `/token/refresh/`
- **Description :** Rafraîchit le jeton d'accès.
- **Corps de la requête :**
  - `refresh` : Jeton de rafraîchissement
- **Permissions :** Aucune
- **Réponse :**
  - Statut 200 OK : Jeton d'accès rafraîchi avec succès
  - Statut 401 UNAUTHORIZED : Rafraîchissement échoué

---

## 2. Tableau (Board)

### Tous les tableaux

- **Méthode :** GET
- **Endpoint :** `/boards/`
- **Description :** Récupère tous les tableaux.
- **Permissions :** Authentification requise
- **Réponse :**
  - Statut 200 OK : Récupération réussie
  - Statut 401 UNAUTHORIZED : Authentification requise

### Nouveau tableau

- **Méthode :** POST
- **Endpoint :** `/board/new/`
- **Description :** Crée un nouveau tableau.
- **Corps de la requête :**
  - `name` : Nom du tableau
  - `description` : Description du tableau
- **Permissions :** Authentification requise
- **Réponse :**
  - Statut 201 CREATED : Création du tableau réussie
  - Statut 400 BAD REQUEST : Entrée invalide ou échec de la création

### Détails du tableau

- **Méthode :** GET
- **Endpoint :** `/board/{id}/`
- **Description :** Récupère un tableau spécifique par ID.
- **Permissions :** Authentification requise
- **Réponse :**
  - Statut 200 OK : Récupération réussie
  - Statut 401 UNAUTHORIZED : Authentification requise
  - Statut 404 NOT FOUND : Tableau non trouvé

### Mise à jour du tableau

- **Méthode :** PATCH
- **Endpoint :** `/board/update/{id}/`
- **Description :** Met à jour les informations du tableau.
- **Corps de la requête :**
  - `name` : Nouveau nom du tableau (optionnel)
  - `description` : Nouvelle description du tableau (optionnel)
- **Permissions :** Authentification requise et auteur du tableau
- **Réponse :**
  - Statut 201 CREATED : Tableau mis à jour avec succès
  - Statut 400 BAD REQUEST : Entrée invalide ou mise à jour échouée
  - Statut 404 NOT FOUND : Tableau non trouvé

### Suppression du tableau

- **Méthode :** DELETE
- **Endpoint :** `/board/delete/{id}/`
- **Description :** Supprime un tableau.
- **Permissions :** Authentification requise et auteur du tableau
- **Réponse :**
  - Statut 200 OK : Tableau supprimé avec succès
  - Statut 400 BAD REQUEST : Échec de la suppression
  - Statut 404 NOT FOUND : Tableau non trouvé

### Ajout d'utilisateur au tableau

- **Méthode :** POST
- **Endpoint :** `/board/add/user/{id}/`
- **Description :** Ajoute un utilisateur au tableau.
- **Corps de la requête :**
  - `id` : ID de l'utilisateur à ajouter
- **Permissions :**

 Authentification requise et auteur du tableau
- **Réponse :**
  - Statut 201 CREATED : Utilisateur ajouté avec succès
  - Statut 400 BAD REQUEST : Entrée invalide ou ajout échoué
  - Statut 404 NOT FOUND : Tableau ou utilisateur non trouvé

### Suppression d'utilisateur du tableau

- **Méthode :** DELETE
- **Endpoint :** `/board/remove/user/{id}/`
- **Description :** Supprime un utilisateur du tableau.
- **Corps de la requête :**
  - `id` : ID de l'utilisateur à supprimer
- **Permissions :** Authentification requise et auteur du tableau
- **Réponse :**
  - Statut 201 CREATED : Utilisateur supprimé avec succès
  - Statut 400 BAD REQUEST : Entrée invalide ou suppression échouée
  - Statut 404 NOT FOUND : Tableau ou utilisateur non trouvé

## 3. Liste (List)

### Toutes les listes pour un tableau

- **Méthode :** GET
- **Endpoint :** `/board/{id}/lists/`
- **Description :** Récupère toutes les listes pour un tableau spécifique.
- **Permissions :** Authentification requise
- **Réponse :**
  - Statut 200 OK : Récupération réussie
  - Statut 401 UNAUTHORIZED : Authentification requise
  - Statut 404 NOT FOUND : Tableau non trouvé

### Nouvelle liste pour un tableau

- **Méthode :** POST
- **Endpoint :** `/board/{id}/list/new/`
- **Description :** Crée une nouvelle liste pour un tableau spécifique.
- **Corps de la requête :**
  - `name` : Nom de la liste
- **Permissions :** Authentification requise et appartenance au tableau
- **Réponse :**
  - Statut 201 CREATED : Création de la liste réussie
  - Statut 400 BAD REQUEST : Entrée invalide ou création échouée
  - Statut 404 NOT FOUND : Tableau non trouvé ou utilisateur non membre

### Détails de la liste

- **Méthode :** GET
- **Endpoint :** `/list/{id}/`
- **Description :** Récupère une liste spécifique par ID.
- **Permissions :** Authentification requise
- **Réponse :**
  - Statut 200 OK : Récupération réussie
  - Statut 401 UNAUTHORIZED : Authentification requise
  - Statut 404 NOT FOUND : Liste non trouvée

### Mise à jour de la liste

- **Méthode :** PATCH
- **Endpoint :** `/list/update/{id}/`
- **Description :** Met à jour les informations de la liste.
- **Corps de la requête :**
  - `name` : Nouveau nom de la liste (optionnel)
- **Permissions :** Authentification requise et appartenance au tableau
- **Réponse :**
  - Statut 201 CREATED : Liste mise à jour avec succès
  - Statut 400 BAD REQUEST : Entrée invalide ou mise à jour échouée
  - Statut 404 NOT FOUND : Liste non trouvée ou utilisateur non membre

### Suppression de la liste

- **Méthode :** DELETE
- **Endpoint :** `/list/delete/{id}/`
- **Description :** Supprime une liste.
- **Permissions :** Authentification requise et appartenance au tableau
- **Réponse :**
  - Statut 200 OK : Liste supprimée avec succès
  - Statut 400 BAD REQUEST : Échec de la suppression
  - Statut 404 NOT FOUND : Liste non trouvée ou utilisateur non membre

## 4. Carte (Card)

### Toutes les cartes pour une liste

- **Méthode :** GET
- **Endpoint :** `/list/{id}/cards/`
- **Description :** Récupère toutes les cartes pour une liste spécifique.
- **Permissions :** Authentification requise
- **Réponse :**
  - Statut 200 OK : Récupération réussie
  - Statut 401 UNAUTHORIZED : Authentification requise
  - Statut 404 NOT FOUND : Liste non trouvée

### Nouvelle carte pour une liste

- **Méthode :** POST
- **Endpoint :** `/list/{id}/card/new/`
- **Description :** Crée une nouvelle carte pour une liste spécifique.
- **Corps de la requête :**
  - `name` : Nom de la carte
  - `description` : Description de la carte
  - `importance` : Importance de la carte
- **Permissions :** Authentification requise et appartenance au tableau
- **Réponse :**
  - Statut 201 CREATED : Création de la carte réussie
  - Statut 400 BAD REQUEST : Entrée invalide ou création échouée
  - Statut 404 NOT FOUND : Liste non trouvée ou utilisateur non membre

### Détails de la carte

- **Méthode :** GET
- **Endpoint :** `/card/{id}/`
- **Description :** Récupère une carte spécifique par ID.
- **Permissions :** Authentification requise
- **Réponse :**
  - Statut 200 OK : Récupération réussie
  - Statut 401 UNAUTHORIZED : Authentification requise
  - Statut 404 NOT FOUND : Carte non trouvée

### Mise à jour de la carte

- **Méthode :** PATCH
- **Endpoint :** `/card/update/{id}/`
- **Description :** Met à jour les informations de la carte.
- **Corps de la requête :**
  - `name` : Nouveau nom de la carte (optionnel)
  - `description` : Nouvelle description de la carte (optionnel)
  - `importance` : Nouvelle importance de la carte (optionnel)
  - `done` : Marquer la carte comme terminée (optionnel)
- **Permissions :** Authentification requise et appartenance au tableau
- **Réponse :**
  - Statut 201 CREATED : Carte mise à jour avec succès
  - Statut 400 BAD REQUEST : Entrée invalide ou mise à jour échouée
  - Statut 404 NOT FOUND : Carte non trouvée ou utilisateur non membre

### Suppression de la carte

- **Méthode :** DELETE
- **Endpoint :** `/card/delete/{id}/`
- **Description :** Supprime une carte.
- **Permissions :** Authentification requise et appartenance au tableau
- **Réponse :**
  - Statut 200 OK : Carte supprimée avec succès
  - Statut 400 BAD REQUEST :Échec de la suppression
  - Statut 404 NOT FOUND : cartr non trouvée ou utilisateur non membre
