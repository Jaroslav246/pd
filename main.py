import json

organizations = []
def load_data():
  file=open('organizations.json', 'r')
  data=json.load(file)
  file.close()
  global organizations
  organizations=data['organizations']
  print('Dati loaded')

def add_organization():
    organization_name=input('Organization nosaukums: ')
    organization_adress=input('Organization adresse: ')
    organization_id=input('Organization id: ')

    organization={
        'name':organization_name,
        'adress':organization_adress,
        'id': organization_id,
            'contacts': []
        }
    while (True):
        response=input('Vai vēlaties pietekties apmeklejumam? (y/n)')
        if response=='y':
            print('Darbinieka informācija:')
            contact_name = input('Ievadiet Darbinieka vārdu: ')
            contact_position = input('Darbinieka adresse: ')
            contact_id = input('Darbinieka id: ')
            sporta_zāle = input('1 dvieļa noma maksā 0,50 eiro: ')
            contact = {
                'name': contact_name,
                'position': contact_position,
                'id': contact_id
            }
            organization['contacts'].append(contact)
        elif response == 'y':
            break
    organizations.append(organization) 

def print_organization():
        for organization in organizations:
            print('---ORGANIZATION---')
            print(f"{organization['name']} ({organization['id']})")
            print(f"Adrese:{organization['adress']}")
            print(f"Kontaktu skaits: {len(organization['contacts'])}")

def save_data():
        data = {
            'organizations': organizations
        }
        print('Saving data...')
        file = open('organizations.json', 'w')
        json.dump(data, file, indent=4)
        print('Data saved')

def find_organization_by_id():
    organization_id=input('Ievadiet organizācijas ID:')
    for organization in organizations:
        if organization['id']==organization_id:
            print('---ORGANIZĀCIJA---')
            print(f"{organization['name']}({organization['id']})")
            break

def count_organizations():
    print(f"Kopējais organizāciju skaits: {len(organizations)}")

def list_organization_ids():
    print("Pieejamie organizāciju ID:")
    for organization in organizations:
        print(organization['id'])

def delete_organization_by_id():
     organization_id = input('Ievadiet organizācijas ID, kuru vēlaties izdzēst: ')
     for i, organization in (organizations):
          if organization['id'] == organization_id:
               del organizations[i]
               print(f"Organizācija ar ID {organization_id} tika izdzēst.")
               return
     print("Organizācija ar šādu ID netika atrasta.")

def main():
        load_data()
        #count_organizations()
        #list_organization_ids()
        #find_organization_by_id()
        #delete_organization_by_id()
        while (True):
            response=input('(1) - Pievieno apmeklētāju // (2) - Izprinte apmeklētāja datus // (3) Iziet: ')
            if response=='1':
                add_organization()
                
                
                
            elif response =='2':
                print_organization()

            elif response=='3':
                save_data()

                print('Paldies, par darbu!')
                print(organizations)
                exit()
            else:
                print('Izvele skaitļu 1,2 vai 3')
                continue
main()