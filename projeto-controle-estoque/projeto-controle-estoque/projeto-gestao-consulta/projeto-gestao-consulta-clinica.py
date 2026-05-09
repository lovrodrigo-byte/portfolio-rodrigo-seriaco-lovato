# Projeto: Gestão de Consultas Médicas
# Desenvolvedor: Rodrigo Seriaco Lovato

def sistema_clinica():
    consultas = []
    
    while True:
        print("\n--- GESTÃO DE CLÍNICA ---")
        print("1. Agendar Consulta")
        print("2. Listar Agendamentos")
        print("3. Cancelar Consulta")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            paciente = input("Nome do Paciente: ").strip().upper()
            horario = input("Horário (ex: 14:30): ")
            consultas.append({"paciente": paciente, "horario": horario})
            print(f"Consulta de {paciente} agendada às {horario}!")
            
        elif opcao == '2':
            print("\n--- LISTA DE CONSULTAS ---")
            if not consultas:
                print("Nenhuma consulta agendada.")
            for i, c in enumerate(consultas):
                print(f"{i+1}. Paciente: {c['paciente']} | Horário: {c['horario']}")
                
        elif opcao == '3':
            if not consultas:
                print("Não há consultas para cancelar.")
                continue
            try:
                idx = int(input("Número da consulta para cancelar: ")) - 1
                removido = consultas.pop(idx)
                print(f"Consulta de {removido['paciente']} cancelada.")
            except (ValueError, IndexError):
                print("Número inválido.")
                
        elif opcao == '4':
            break

if __name__ == "__main__":
    sistema_clinica()
