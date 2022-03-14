# module 6/7 - POO - Parc auto

# 1
# Création class Vehicule (attributs, constructeur, méthodes)
# 2
# Encapsulation sur la class Vehicule : attributs privés (double underscore). Méthodes en public (par défaut)
# Méthodes d'accès en lecture (getters) et écritures (setters)
# 3
# Implémentation d'unc compteur d'instances via des membres de classe
# 4 Héritage, exceptions...
# 5 Implémentation d’un comparateur d’objets Vehicule
from parc.exceptions import VehiculeException


class Vehicule:

    __marque = ""
    __modele = ""
    __vitesse = 0
    __vitesse_max = 0
    __nb_vehicules = 0

    # Constructeur (initialisation des 4 attributs de la classe Vehicule)
    def __init__(self, marque, modele, vitesse, vitesse_max):
        self.__marque = marque
        self.__modele = modele
        self.__vitesse = vitesse
        self.__vitesse_max = vitesse_max

        # Incrémentation du compteur d'objets
        # /!\ pas " self.__nb_vehicules " car nb_vehicule esst un attribut de classe, non d'instance.
        # On y accède donc par le nom de la classe (combien de vehicules ont été crées via la classe Vehicule...)
        Vehicule.__nb_vehicules += 1

    # Méthodes

    # Redéfinir la méthode __eq()__ pour tester les doublons de véhicules lors de leur création
    def __eq__(self, other):
        # Toujours commencer par tester que Other n'est pas égal à None et est bien de type Vehicule
        if other is not None and isinstance(other, Vehicule) \
            and self.__marque == other.__marque \
            and self.__modele == other.__modele \
            and self.__vitesse == other.__vitesse \
            and self.__vitesse_max == other.__vitesse_max: \
                return True
        return False

    def accelerer(self):
        if self.__vitesse < self.__vitesse_max:  # Paramètre auto "self" -> réfère à l'objet courant
            self.__vitesse += 1
        else:
            raise VehiculeException("Vitesse maximum atteinte !")

    def freiner(self):
        if self.__vitesse > 0:
            self.__vitesse -= 1
        else:
            raise VehiculeException("Véhicule à l'arrêt.")

    # -> Getters
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_vitesse(self):
        return self.__vitesse

    def get_vitesse_max(self):
        return self.__vitesse_max

    # -> Setters
    def set_vitesse_max(self, vitesse_max):
        if 0 < vitesse_max < self.__vitesse_max:  # si vitesse > 0 et inférieure à vitesse max
            self.__vitesse_max = vitesse_max
        else:
            raise VehiculeException("Valeur de vitesse maximum incohérente !")

    # Définition de la méthode de classe permettant l'accès au nb de véhicules
    # @classmethod pour méthode de classe, avec 1er paramètres " cls "
    @classmethod
    def get_nb_vehicules(cls):
        return cls.__nb_vehicules
        # = return Vehicule.__nb_vehicules


# Démonstration héritage

class Voiture(Vehicule):
    __qte_carburant = 0
    __qte_carburant_max = 0
    __nb_places = 0

    # Constructeur (initialisation des attributs)
    # -> attributs hérités de Vehicule
    # -> attributs propres à Voiture
    def __init__(self, marque, modele, vitesse, vitesse_max, qte_carburant, qte_carburant_max, nb_places, energie):
        # self.__marque = marque -> /!\ : marque est privé dans Vehicule
        # On appelle donc le constructeur de la super classe. Attention, il faut passer le paramètre self :
        Vehicule.__init__(self, marque, modele, vitesse, vitesse_max)

        # Initialisation
        if nb_places > 0:
            self.__nb_places = nb_places

        if 0 < qte_carburant < qte_carburant_max:
            self.__qte_carburant = qte_carburant

        if qte_carburant_max > 0:
            self.__qte_carburant_max = qte_carburant_max

        # Composition : le cycle de vie est lié : lorsqu'on créer une Voiture, on créer le Moteur
        self.__moteur = Moteur(energie)

# Méthodes : (s'ajoutent à celles héritées de Vehicule)
    def faire_le_plein(self):
        self.__qte_carburant = self.__qte_carburant_max

    def get_qte_carburant(self):
        return self.__qte_carburant

    def get_qte_carburant_max(self):
        return self.__qte_carburant_max

    def get_nb_places(self):
        return self.__nb_places

    def get_moteur(self):
        return self.__moteur

# 2 Redéfinition de la méthode accelerer() en prenant en compte la qte de carburant consommée :
    def accelerer(self):
        if self.__qte_carburant > 0:
            # A l'appel de la méthode accelerer() de Vehicule, /!\ on passe le param Self
            Vehicule.accelerer(self)
            self.__qte_carburant -= 1


# Classes Moto et Velo
class Moto(Vehicule):
    __cylindree = 0

    def __init__(self, marque, modele, vitesse, vitesse_max, cylindree):
        Vehicule.__init__(self, marque, modele, vitesse, vitesse_max)
        if cylindree > 0:
            self.__cylindree = cylindree

        def get_cylindree(self):
            return self.__cylindree


class Velo(Vehicule):
    __type = ""

    def __init__(self, marque, modele, vitesse, vitesse_max, type):
        Vehicule.__init__(self, marque, modele, vitesse, vitesse_max)
        # "in" keyword is used to check if a value is present in a sequence :
        if type in ("course", "VTT", "VTC"):
            self.__type = type
        else:
            raise VehiculeException("Type de vélo incorrect.")

    def get_type(self):
        return self.__type


class Moteur:
    __energie = ""

    def __init__(self, energie):
        if energie in ("Diesel", "SP95", "SP98"):
            self.__energie = energie

    def get_energie(self):
        return self.__energie






