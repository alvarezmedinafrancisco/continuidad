import flet as ft 

def main(page: ft.Page):
    page.title = "Formulario"
    page.padding = 20
    

    title = ft.Text("inicio de sesion", size=28, weight=ft.FontWeight.BOLD)
    name = ft.TextField(label="ingresa tu nombre y apellidos", hint_text="Ingrese el nombre", width=400)
    contra = ft.TextField(label="ingresa tu contraseña", hint_text="Ingrese el nombre", width=400, password=True)
    confirmar_contraseña =  ft.TextField(label="ingresa tu contraseña", hint_text="Ingrese el nombre", width=400, password=True)
    modality = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial",
    )
    #agregar una funcion para usar el navbar o algo asi 
    #investigar que es y como se usa el modelo vista controlador y porque se usa en cualquier lenguaje de programacion y tiene sus detallitos pero nosotros vamos a trabajar python con flet 
    
    inscription = ft.Checkbox(label="Requiere inscripción previa", value=False )
    duration_slider = ft.Slider(min=1, max=8, divisions=7, value=2, label="2 h", width=300)
    
    def on_duration_change(e):
        duration_slider.label = f"{int(e.control.value)} h"
        duration_slider.update()
        
    duration_slider.on_change = on_duration_change
    summary_container = ft.Column()
    
    def show_summary(e):
        if not name.value or name.value.strip() == "":
            name.error_text = "El  campo nombre no puede estar vacío"
            name.update()
            summary_container.controls = [ft.Text("la contraseña es diferente.", color=ft.Colors.RED)]
            summary_container.update()
            return
            
        name.error_text = None
        name.update()
        
        
        lines = [
            ft.Text("Resumen del Evento", size=20, weight=ft.FontWeight.BOLD),
            ft.Text(f"Nombre: {name.value}", size=16),
            ft.Text(f"Modalidad: {modality.value}", size=16),
            ft.Text(f"Requiere inscripción previa: {'Sí' if inscription.value else 'No'}", size=16),
            ft.Text(f"Duración estimada: {int(duration_slider.value)} h", size=16),
        ]
        summary_container.controls = [ft.Divider()] + lines
        summary_container.update()
        
    show_button = ft.ElevatedButton(
        content=ft.Text("iniciar sesion", color=ft.Colors.WHITE), 
        bgcolor=ft.Colors.BLUE_600, 
        on_click=show_summary,
    )
    
    form = ft.Column(
        [
            title,
            name,
            contra,
            confirmar_contraseña,
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