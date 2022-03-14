# Module 6 - POO - Instanciation d'une classe
from parc.classes import Vehicule, Voiture, Moto, Velo
from parc.exceptions import VehiculeException

if __name__ == "__main__":

    # 1

    # Lecture compteur de véhicules
    print("Nombre de véhicules : {}".format(Vehicule.get_nb_vehicules()))

    # Créa d'1 objet 'Vehicule' + try

    try:
        v1 = Vehicule("Citroen", "C4", 180, 180)
        print("Vitesse : {}".format(v1.get_vitesse()))  # on met le getter car accès direct privé
        print("Nombre de véhicules : {}".format(Vehicule.get_nb_vehicules()))

        # Appel des méthodes
        v1.accelerer()
        print("Vitesse après accélération : {}".format(v1.get_vitesse()))
    except VehiculeException as e:
        print('Erreur sur le Vehicule ! Message : {}'.format(e))

        v1.freiner()
        print("Vitesse après freinage : {}".format(v1.get_vitesse()))

    v2 = Vehicule("BMW", "700", 70, 200)
    v3 = Vehicule("audi", "A4", 70, 200)

    print("Nombre de véhicules : {}\n".format(Vehicule.get_nb_vehicules()))

    # 2 Instance de Voiture héritant de Vehicule
    try:
        car1 = Voiture("Renault", "Scenic", 60, 170, 32, 50, 5, "Diesel")
        print("(Getters + Moteur/energie) La {} {} roule à {} km/h et son réservoir contient "
              "{} litres de carburant {}.".format(
            car1.get_marque(),
            car1.get_modele(),
            car1.get_vitesse(),
            car1.get_qte_carburant(),
            car1.get_moteur().get_energie()
        ))
        # Test méthode accelerer()
        car1.accelerer()
        print("(Accélération) La {} {} roule à {} km/h et son réservoir contient {} litres de carburant.".format(
            car1.get_marque(),
            car1.get_modele(),
            car1.get_vitesse(),
            car1.get_qte_carburant()
        ))
        car1.accelerer()
        print("(Accélération) La {} {} roule à {} km/h et son réservoir contient {} litres de carburant.".format(
            car1.get_marque(),
            car1.get_modele(),
            car1.get_vitesse(),
            car1.get_qte_carburant()
        ))
    except VehiculeException as e:
        print("Erreur sur la Voiture ! Message : {}".format(e))

    # Test méthode freiner()
    car1.freiner()
    print("(Freinage) La {} {} roule à {} km/h et son réservoir contient {} litres de carburant.".format(
        car1.get_marque(),
        car1.get_modele(),
        car1.get_vitesse(),
        car1.get_qte_carburant()
    ))
    # Test méthode faire_le_plein()
    car1.faire_le_plein()
    print("(Plein) Le réservoir de la {} {}  contient {} litres de carburant".format(
        car1.get_marque(),
        car1.get_modele(),
        car1.get_qte_carburant()
    ))
    # Nombre de place
    car1.get_nb_places()
    print("(Nombre de places) La {} {} possède {} places.".format(
        car1.get_marque(),
        car1.get_modele(),
        car1.get_nb_places()
    ))

    print("\n")

    # Moto
    moto1 = Moto("Harley Davidson", "CVO", 100, 200, 1868)
    print("Cette moto est de la marque {}.".format(
        moto1.get_marque()
    ))
    moto1.freiner()
    print("(Freinage) La {} {} roule maintenant à {} km/h.".format(
        moto1.get_marque(),
        moto1.get_modele(),
        moto1.get_vitesse(),
    ))

    # test __eq__
    print("\n")
    v4 = Vehicule("Peugeot", "308", 50, 180)
    v5 = Vehicule("Peugeot", "308", 50, 180)
    v6 = Vehicule("Opel", "Astra", 60, 180)

    print("v4 == v5 ? ", v4 == v5)
    print("v4 == v6 ? ", v4 == v6)
    print("v5 == v6 ? ", v5 == v6)

    # Gestion exceptions sur chaque type de Vehicule créé
    try:
        print("\n")
        print("Vélos :")
        velo1 = Velo("marqueVelo", "modeleVelo", 30, 70, "VT")
        print("Le {} {} de type {}, roule à {} km/h.".format(
            velo1.get_marque(),
            velo1.get_modele(),
            velo1.get_type(),
            velo1.get_vitesse()
        ))
        velo1.accelerer()
        print("(accélération) Le {} {} de type {}, roule à {} km/h.".format(
            velo1.get_marque(),
            velo1.get_modele(),
            velo1.get_type(),
            velo1.get_vitesse()
        ))
    except VehiculeException as e:
        print("Erreur (VehiculeException) ! Message : {}.".format(e))


