import flet as ft 

def main(page: ft.Page):
    page.title = "Formulario"
    page.padding = 20
    
    # Corregí un poquito la ortografía en los textos para que se vea más pro
    title = ft.Text("Inicio de sesión", size=28, weight=ft.FontWeight.BOLD)
    name = ft.TextField(label="Ingresa tu nombre y apellidos", hint_text="Ingrese el nombre", width=400)
    contra = ft.TextField(label="Ingresa tu contraseña", hint_text="Contraseña", width=400, password=True)
    confirmar_contraseña = ft.TextField(label="Confirma tu contraseña", hint_text="Contraseña", width=400, password=True)
    correo = ft.TextField(label="correo", hint_text="correo", width=400)
    
    modality = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial",
    )
    
    inscription = ft.Checkbox(label="Requiere inscripción previa", value=False)
    duration_slider = ft.Slider(min=1, max=8, divisions=7, value=2, label="2 h", width=300)
    
    def on_duration_change(e):
        duration_slider.label = f"{int(e.control.value)} h"
        duration_slider.update()
        
    duration_slider.on_change = on_duration_change
    summary_container = ft.Column()
    
    def show_summary(e):
        # 1. Validamos que el nombre no esté vacío
        if not name.value or name.value.strip() == "":
            name.error_text = "El campo nombre no puede estar vacío"
            name.update()
            summary_container.controls = [ft.Text("Llena el nombre para continuar.", color=ft.Colors.RED)]
            summary_container.update()
            return
        else:
            name.error_text = None
            name.update()
            
        # 2. Validamos que las contraseñas coincidan y no estén vacías
        if not contra.value or contra.value != confirmar_contraseña.value:
            contra.controls = [ft.Text("las contraseñas no coinciden.", color=ft.Colors.RED)]
            confirmar_contraseña.controls = [ft.Text("las contraseñas no coinciden.", color=ft.Colors.RED)]
            contra.update()
            confirmar_contraseña.update()
            summary_container.controls = [ft.Text("Hay un error en las contraseñas.", color=ft.Colors.RED)]
            summary_container.update()
            return
        else:
            # Si sí coinciden, quitamos las letras rojas de error
            contra.error_text = None
            confirmar_contraseña.error_text = None
            contra.update()
            confirmar_contraseña.update()

        
        # 3. Si pasó las dos pruebas de arriba, mostramos el resumen
        lines = [
            ft.Text("¡Todo bien! Resumen del Evento:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
            ft.Text(f"Nombre: {name.value}", size=16),
            ft.Text(f"Modalidad: {modality.value}", size=16),
            ft.Text(f"Requiere inscripción previa: {'Sí' if inscription.value else 'No'}", size=16),
            ft.Text(f"Duración estimada: {int(duration_slider.value)} h", size=16),
        ]
        summary_container.controls = [ft.Divider()] + lines
        summary_container.update()
        
    show_button = ft.ElevatedButton(
        content=ft.Text("Iniciar sesión", color=ft.Colors.WHITE), 
        bgcolor=ft.Colors.BLUE_600, 
        on_click=show_summary,
    )
    
    form = ft.Column(
        [
            title,
            name,
            contra,
            confirmar_contraseña,
            correo,
            ft.Row([ft.Text("Modalidad:"), modality], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            inscription,
            ft.Row([ft.Text("Duración:"), duration_slider], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            show_button,
            summary_container,
        ],
        tight=True,
        spacing=12,
        scroll=ft.ScrollMode.ADAPTIVE,
    )

    page.add(form)

if __name__ == "__main__":
    ft.app(target=main)
    