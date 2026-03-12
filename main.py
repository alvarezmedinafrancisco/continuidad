import flet as ft 

def main(page: ft.Page):
    page.title = "Formulario"
    page.padding = 20
    
    title = ft.Text("Registro de Evento", size=28, weight=ft.FontWeight.BOLD)
    name_field = ft.TextField(label="Nombre del evento", hint_text="Ingrese el nombre del evento", width=400)
    dropdown = ft.Dropdown(
        label="Tipo de evento",
        hint_text="Selecciona el tipo",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Seminario"),
        ],
        width=400,
    )

    modality = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial",
    )
    
    inscription = ft.Checkbox(label="Requiere inscripción previa", value=False )
    duration_slider = ft.Slider(min=1, max=8, divisions=7, value=2, label="2 h", width=300)
    
    def on_duration_change(e):
        duration_slider.label = f"{int(e.control.value)} h"
        duration_slider.update()
        
    duration_slider.on_change = on_duration_change
    summary_container = ft.Column()
    
    def show_summary(e):
        if not name_field.value or name_field.value.strip() == "":
            name_field.error_text = "El nombre del evento no puede estar vacío"
            name_field.update()
            summary_container.controls = [ft.Text("Corrija los errores antes de continuar.", color=ft.Colors.RED)]
            summary_container.update()
            return
            
        name_field.error_text = None
        name_field.update()
        
        tipo_evento = dropdown.value if dropdown.value else "No especificado"
        
        lines = [
            ft.Text("Resumen del Evento", size=20, weight=ft.FontWeight.BOLD),
            ft.Text(f"Nombre: {name_field.value}", size=16),
            ft.Text(f"Tipo: {tipo_evento}", size=16),
            ft.Text(f"Modalidad: {modality.value}", size=16),
            ft.Text(f"Requiere inscripción previa: {'Sí' if inscription.value else 'No'}", size=16),
            ft.Text(f"Duración estimada: {int(duration_slider.value)} h", size=16),
        ]
        summary_container.controls = [ft.Divider()] + lines
        summary_container.update()
        
    show_button = ft.ElevatedButton(
        content=ft.Text("Mostrar resumen", color=ft.Colors.WHITE), 
        bgcolor=ft.Colors.BLUE_600, 
        on_click=show_summary,
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    form = ft.Column(
        [
            title,
            name_field,
            show_button,
            dropdown,
            ft.Row([ft.Text("Modalidad:"), modality], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            inscription,
            ft.Row([ft.Text("Duración:"), duration_slider], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            
            summary_container,
        ],
        tight=True,
        spacing=12,
        scroll=ft.ScrollMode.ADAPTIVE,
    )

    page.add(form)

if __name__ == "__main__":
    ft.app(target=main)