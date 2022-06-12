# ProxiDoc
Une plateforme, qui permet à une personne de prendre rendez-vous avec un médecin en ligne dans sa zone de résidence ou à proximité. 
## Modélisation

### Patient

- Nom
- Prénom
- Date de naissance
- Sexe
- Adresse
- Position géographique
- Numéro téléphone
- Email
- Mot de passe

### Médecin

- ID: Identifiant unique du médecin
- Photocopie d’identité ou passeport
- Photo: Photo du médecin -Nom: Nom du médecin
- Prénom: Prénom du médecin
- Sexe: Homme ou Femme
- Adresse: Adresse du médecin
- Numéro téléphone: Numéro de téléphone du médecin
- Email: Email du médecin
- Mot de passe: Mot de passe du médecin
- Position géographique: Position géographique du médecin
- Spécialité: Spécialité du médecin -Statuts: Statuts du médecin

### Rendez-vous

- Code: Code unique du rendez-vous
- Libellé: Libellé du rendez-vous
- Date: Date du rendez-vous -Durée: Durée du rendez-vous
- Lien: Lien du rendez-vous

## Services

- Gestion des comptes pour les patients
    - Créer un compte, se connecter et mettre à jour les détails du compte, suppression compte
    - Les patients peuvent voir les médecins qui les entourent
    - Les patients doivent pouvoir envoyer des demandes de rendez-vous
    - Les patients peuvent conserver une trace des rendez-vous qu'ils prennent.
- Gestion des comptes pour les médecins
    - Mettre à jour son mot de passe et son adresse
    - Les médecins peuvent gérer les demandes de rendez-vous via leurs portails.
    - Possibilité pour les médecins de répondre aux demandes de rendez-vous
    - Les médecins peuvent également être en mesure de suivre les dossiers des rendez-vous qu'ils ont pris
    - Les médecins peuvent basculer entre les moments où ils sont disponibles ou indisponibles pour prendre rendez-vous.
