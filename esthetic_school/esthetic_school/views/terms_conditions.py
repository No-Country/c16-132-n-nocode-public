import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.navbar import navbar
from esthetic_school.routes import Route

@rx.page(route=Route.TERMS_CONDITIONS.value, title="Terminos y Condiciones")
def terms_conditions() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            rx.vstack(
                heading(
                    "Terminos y Condiciones", 
                    True
                ),
                rx.vstack(
                    rx.section(
                        heading("1. Introducción"),
                        rx.text("Bienvenido a Esthetic School. Estos términos y condiciones (Terminos) rigen el uso de nuestra plataforma en" 
                                "línea que ofrece cursos de estética y belleza (Servicios). Al acceder o utilizar nuestros" 
                                "Servicios, aceptas estar legalmente obligado por estos Términos. Si no estás de acuerdo con" 
                                "alguno de los términos, no utilices nuestros Servicios."),
                        ),
                    rx.section(
                        heading("2. Registro y Cuentas de Usuario"),
                        rx.text("2.1. Para acceder a ciertas características de nuestros Servicios, es posible que necesites registrarte y crear una cuenta de usuario. Debes proporcionar información precisa y completa durante el proceso de registro y mantener tu información de cuenta actualizada en todo momento."),
                        rx.text("2.2. Eres responsable de mantener la confidencialidad de tu contraseña y de cualquier actividad que ocurra en tu cuenta. Notifícanos inmediatamente si sospechas de cualquier uso no autorizado de tu cuenta")
                    ),
                    rx.section(
                        heading("3. Cursos y Pagos"),
                        rx.text("3.1. Nuestros cursos están diseñados para proporcionar educación en el campo de la estética y la belleza. Hacemos todo lo posible para garantizar la precisión y la calidad de nuestro contenido, pero no garantizamos resultados específicos."),
                        rx.text("3.2. Los cursos pueden estar disponibles de forma gratuita o mediante pago. Al inscribirte en un curso de pago, aceptas pagar la tarifa correspondiente según lo establecido en nuestro sitio web. Las tarifas son no reembolsables a menos que se indique lo contrario en nuestros Términos de reembolso.")
                    ),

                    rx.section(
                        heading("4. Propiedad Intelectual"),
                        rx.text("4.1. Todos los derechos de propiedad intelectual relacionados con nuestros Servicios, incluidos, entre otros, los derechos de autor, marcas comerciales y derechos de base de datos, son propiedad de Esthetic School o de nuestros licenciantes."),
                        rx.text("4.2. No tienes derecho a copiar, modificar, distribuir, transmitir, mostrar, realizar, reproducir, publicar, licenciar, crear trabajos derivados, transferir o vender ningún contenido, software, productos o servicios obtenidos de nuestros Servicios sin nuestro consentimiento previo por escrito.")
                    ),

                    rx.section(
                        heading("5. Conducta del Usuario"),
                        rx.text("5.1. Te comprometes a utilizar nuestros Servicios solo para fines legales y de conformidad con estos Términos. No debes utilizar nuestros Servicios de ninguna manera que pueda dañar, deshabilitar, sobrecargar o deteriorar el rendimiento de nuestros Servicios."),
                        rx.text("5.2. No debes enviar ningún contenido que sea ilegal, ofensivo, difamatorio, obsceno o que infrinja los derechos de propiedad intelectual de terceros.")
                    ),

                    rx.section(
                        heading("6. Modificaciones y Terminación"),
                        rx.text("6.1. Nos reservamos el derecho de modificar, suspender o descontinuar cualquier parte de nuestros Servicios en cualquier momento y sin previo aviso."),
                        rx.text("6.2. Nos reservamos el derecho de terminar tu acceso a nuestros Servicios si consideramos que has violado estos Términos o cualquier ley aplicable.")
                    ),

                    rx.section(
                        heading("7. Limitación de Responsabilidad"),
                        rx.text("7.1. En la máxima medida permitida por la ley, Esthetic School no será responsable por ningún daño directo, indirecto, incidental, especial, consecuente o punitivo, incluidos, entre otros, la pérdida de ingresos, beneficios, datos, uso o cualquier otra pérdida intangible, resultante de tu acceso o uso de nuestros Servicios."),
                    ),

                    rx.section(
                        heading("8. Ley Aplicable y Jurisdicción"),
                        rx.text("8.1. Estos Términos se regirán e interpretarán de acuerdo con las leyes del país donde está ubicada nuestra empresa, sin tener en cuenta sus disposiciones sobre conflictos de leyes."),
                        rx.text("8.2. Cualquier disputa que surja de estos Términos estará sujeta a la jurisdicción exclusiva de los tribunales de la misma jurisdicción que se menciona en la cláusula 8.1.")
                    ),

                    rx.section(
                        heading("9. Disposiciones Generales"),
                        rx.text("9.1. Si alguna disposición de estos Términos se considera inválida, ilegal o inexigible, dicha disposición se considerará separable de estos Términos y no afectará la validez y aplicabilidad de las disposiciones restantes."),
                        rx.text("9.2. Estos Términos constituyen el acuerdo completo entre tú y Esthetic School con respecto a tu uso de nuestros Servicios, y reemplazan cualquier acuerdo previo o contemporáneo, ya sea oral o escrito, en relación con el mismo.")
                    ),
                    rx.section(
                        heading("10. Contacto"),
                        rx.text("Si tienes alguna pregunta sobre estos Términos, puedes contactarnos en estheticschool@gmail.com."),
                        rx.text("Gracias por elegir Esthetic School. ¡Esperamos que disfrutes aprendiendo con nosotros!")
                    ),
                    spacing="0",
                    
                ),
                align="center",
                margin_top="2em",
                height="80vh",
                width="80%",
                spacing="1"
            ),
            align="center",
            justify="center",
        )
    )