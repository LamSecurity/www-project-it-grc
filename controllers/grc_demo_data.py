#-----------------------------------------------------
# Demo data to upload to database
#-----------------------------------------------------

def _load_demo_data():
    #-----------
    # Users
    #-----------
    db.auth_user.update_or_insert((db.auth_user.id==1),id=1, first_name="admin", last_name="admin", email="admin@email.com", username="admin", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==2),id=2, first_name="guest", last_name="guest", email="guest@email.com", username="guest", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==3),id=3, first_name="riskManager", last_name="riskManager", email="riskManager@email.com", username="riskManager", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==4),id=4, first_name="riskAnalyst", last_name="riskAnalyst", email="riskAnalyst@email.com", username="riskAnalyst", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==5),id=5, first_name="auditManager", last_name="auditManager", email="auditManager@email.com", username="auditManager", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==6),id=6, first_name="auditAnalyst", last_name="auditAnalyst", email="auditAnalyst@email.com", username="auditAnalyst", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==7),id=7, first_name="processOwner", last_name="processOwner", email="processOwner@email.com", username="processOwner", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==8),id=8, first_name="controlResp", last_name="controlResp", email="controlResp@email.com", username="controlResp", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==9),id=9, first_name="informationOwner", last_name="informationOwner", email="informationOwner@email.com", username="informationOwner", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==10),id=10, first_name="itAdmin", last_name="itAdmin", email="itAdmin@email.com", username="itAdmin", password=db.auth_user.password.validate('Password01')[0])
    db.auth_user.update_or_insert((db.auth_user.id==11),id=11, first_name="riskOwner", last_name="riskOwner", email="riskOwner@email.com", username="riskOwner", password=db.auth_user.password.validate('Password01')[0])
    #--------
    # Groups
    #--------
    db.auth_group.update_or_insert((db.auth_group.id==1),id=1, role="admin", description="admin")
    db.auth_group.update_or_insert((db.auth_group.id==2),id=2, role="guest", description="guest")
    db.auth_group.update_or_insert((db.auth_group.id==3),id=3, role="riskManager", description="riskManager")
    db.auth_group.update_or_insert((db.auth_group.id==4),id=4, role="riskAnalyst", description="riskAnalyst")
    db.auth_group.update_or_insert((db.auth_group.id==5),id=5, role="auditManager", description="auditManager")
    db.auth_group.update_or_insert((db.auth_group.id==6),id=6, role="auditAnalyst", description="auditAnalyst")
    db.auth_group.update_or_insert((db.auth_group.id==7),id=7, role="processOwner", description="processOwner")
    db.auth_group.update_or_insert((db.auth_group.id==8),id=8, role="controlResp", description="controlResp")
    db.auth_group.update_or_insert((db.auth_group.id==9),id=9, role="informationOwner", description="informationOwner")
    db.auth_group.update_or_insert((db.auth_group.id==10),id=10, role="itAdmin", description="itAdmin")
    db.auth_group.update_or_insert((db.auth_group.id==11),id=11, role="riskOwner", description="riskOwner")
    #-----------
    # Membership
    #-----------
    db.auth_membership.update_or_insert((db.auth_membership.id==1),id=1, user_id=1, group_id=1)
    db.auth_membership.update_or_insert((db.auth_membership.id==2),id=2, user_id=2, group_id=2)
    db.auth_membership.update_or_insert((db.auth_membership.id==3),id=3, user_id=3, group_id=3)
    db.auth_membership.update_or_insert((db.auth_membership.id==4),id=4, user_id=4, group_id=4)
    db.auth_membership.update_or_insert((db.auth_membership.id==5),id=5, user_id=5, group_id=5)
    db.auth_membership.update_or_insert((db.auth_membership.id==6),id=6, user_id=6, group_id=6)
    db.auth_membership.update_or_insert((db.auth_membership.id==7),id=7, user_id=7, group_id=7)
    db.auth_membership.update_or_insert((db.auth_membership.id==8),id=8, user_id=8, group_id=8)
    db.auth_membership.update_or_insert((db.auth_membership.id==9),id=9, user_id=9, group_id=9)
    db.auth_membership.update_or_insert((db.auth_membership.id==10),id=10, user_id=10, group_id=10)
    db.auth_membership.update_or_insert((db.auth_membership.id==11),id=11, user_id=11, group_id=11)
    #--------------------
    # Risk Classification
    #--------------------
    db.risk_classification.update_or_insert((db.risk_classification.id==1), id=1, name="Operational (Operacional)", description="Risks that affect the ability of the organization to achieve its strategic plans. They can provoke losses to the Company due to human errors, inadequate or defective internal processes, failures in the systems, etc. (Riesgos que afectan la habilidad de la organización para lograr el plan estratégico. El riesgo operacional es el tipo de riesgo que puede provocar pérdidas a la Organizacion debido a errores humanos, procesos internos inadecuados o defectuosos.)", risk_manager_approval='T')
    db.risk_classification.update_or_insert((db.risk_classification.id==2), id=2, name="Strategic (Estratégico)", description="Risks derived from incorrect decision-making and/or from the inability to response to the changes happening in the industry. It determines the compatibility of the strategic objectives of the Company, the developed strategies to reach said objectives, the used resources and the quality of their Execution, examples: economic, technological, competitive and regulatory changes. The General Management C-suite identifies the most important risks which are then approved by the Committee. (El riesgo estratégico deriva de la aplicación indebida de las decisiones, o la falta de capacidad de respuesta a los cambios de la industria. Este riesgo es una función de la compatibilidad de los objetivos estratégicos de la Organizacion, las estrategias desarrolladas para alcanzar dichos objetivos, los recursos utilizados, así como la calidad de su ejecución, ejemplo: cambios económicos, tecnológicos, competitivos y regulatorios. La alta gerencia C-suite identifica los riesgos más importantes a través del proceso de planificación y obtiene aprobación de la Junta.)", risk_manager_approval='T')
    db.risk_classification.update_or_insert((db.risk_classification.id==3), id=3, name="Compliance (Cumplimiento)", description="The risk of Infringement to the current legal dispositions, norms, organisms, regulatory institutions, adopted standards by the Company and codes of conduct applicable to the activities of the Company that can lead to sanctions and/or reputational damage that subsequently impacts the results, capital, expectations of the development of the business. (Es el riesgo del cumplimiento de las disposiciones legales, normas, organismos, instituciones reguladoras, estándares adoptados por la organización y códigos de conducta aplicables a las actividades de la Organización, que puede conllevar sanciones y/o deterioros de reputación, provocando en consecuencia un impacto adverso en los resultados, y/o en el capital, y/o en las expectativas de desarrollo de los negocios de la Organización.)", risk_manager_approval='T')
    db.risk_classification.update_or_insert((db.risk_classification.id==4), id=4, name="Financial (Financiero)", description="The risk of an inopportune event or financial fluctuation that bring negative consequences to the Company, for example: valuation, market risks, credits, liquidity, leverage, debts, etc. (El riesgo financiero es la probabilidad de que un evento adverso o alguna fluctuación financiera reporte consecuencias negativas en una empresa, ejemplo: información financiera, valoración, cobertura, apalancamiento, deuda, riesgos de mercado y liquidez, y riesgos de crédito en instituciones financieras.)", risk_manager_approval='T')
    db.risk_classification.update_or_insert((db.risk_classification.id==5), id=5, name="IT (TI)", description="Risks that are related to the IT elements that process, store or transmit sensible information or that support critical processes of the Company. (Riesgos relacionados a elementos de TI que procesan, almacenan o transmiten información sensible, o que soportan procesos críticos en la organización.)", risk_manager_approval='T')
    #----------------------
    # Risk Treatment
    #----------------------
    db.risk_treatment.update_or_insert((db.risk_treatment.id==1), id=1, name="Mitigar (Mitigate)", description="Measures taken to reduce the probability or occurrence of the risk as well to reduce its impact in case of occurence. In general, it involves the multiple business decisions that are made daily in an organization. (Se adoptan medidas para reducir la probabilidad o el impacto del riesgo o ambos; por lo general, puede conllevar cualquiera de las múltiples decisiones de negocio que se adoptan en el día a día de una organización.)", risk_manager_approval='T')
    db.risk_treatment.update_or_insert((db.risk_treatment.id==2), id=2, name="Aceptar (Accept)", description="No measure is taken to decrease the probability or impact of the risk. (No se adopta ninguna medida que afecte a la probabilidad o al impacto del riesgo.)", risk_manager_approval='T')
    db.risk_treatment.update_or_insert((db.risk_treatment.id==3), id=3, name="Evitar (Avoid)", description="The activites that give rise to the risk are abandoned; which can lead to the abandonment of a production line, a limited expansion in a new geographic market or the sale of a business segment. (Se abandonan las actividades que den lugar al riesgo; esto puede conllevar que se abandone una línea de producción, que se reduzca el grado de expansión en un nuevo mercado geográfico o que se venda una división.)", risk_manager_approval='T')
    db.risk_treatment.update_or_insert((db.risk_treatment.id==4), id=4, name="Compartir (Transfer)", description="The probability or impact of the risk is reduced by handing it over or shared with a third party, such as, the suscription of insurances or outsourcing an activitiy. (Se reduce la probabilidad o el impacto al riesgo transfiriendo o compartiendo de cualquier otra manera una parte del riesgo; las técnicas que se utilizan más habitualmente incluyen la suscripción de seguros, el establecimiento de negocios, la cobertura de transacciones o la externalización de una actividad.)", risk_manager_approval='T')
    #-------------------------
    # Organization Department 
    #-------------------------   
    db.department.update_or_insert((db.department.id==1), id=1, name="IT (TI)", description='', responsible="Responsible 1", risk_manager_approval='T')
    db.department.update_or_insert((db.department.id==2), id=2, name="Marketing (Mercadotecnia)",  description='', responsible="Responsible 2", risk_manager_approval='T')
    db.department.update_or_insert((db.department.id==3), id=3, name="Operations (Operaciones)", description='', responsible="Responsible 3", risk_manager_approval='T')
    #------------------
    # Process Type
    #------------------
    db.process_type.update_or_insert((db.process_type.id==1), id=1, name="NA", description="NA", risk_manager_approval='T')
    db.process_type.update_or_insert((db.process_type.id==2), id=2, name="Strategic (Estratégico)", description="Processes that define the guidelines, objectives and policies of an organization. The processes define the strategies of the organizations and, in general, are the responsibility of the upper management. They relate to the vision of the organization. (Procesos que definen las pautas, objetivos y politicas de una organización. Los procesos definen las estrategias de las organizaciones y, por lo general, son responsabilidad de los altos mandos. Se relacionan con la visión de la organización.)", risk_manager_approval='T')
    db.process_type.update_or_insert((db.process_type.id==3), id=3, name="Operative (Operativo)", description="Processes that generate the product or service that will be given to the client; therefore, they are considered to make up the organization's value chain. The different departments or areas of the organization, with all their human resources, are responsible for carrying them out. They help fulfill the mission of the company. (Procesos que generan el producto o servicio que se le dará al cliente; por ello, se considera que conforman la cadena de valor de la organización. Los diferentes departamentos o áreas de la organización, con todos sus recursos humanos, son responsables de realizarlos. Ayudan a cumplir la misión de la empresa.)", risk_manager_approval='T')
    db.process_type.update_or_insert((db.process_type.id==4), id=4, name="Support (Soporte)", description="Processes serve to control and improve the management of the company, as well as help other processes to be carried out. Support processes do not directly create products or services but are necessary to facilitate or assist the execution of operating or management processes. (Procesos de sirven para controlar y mejorar la gestión de la empresa, así como ayudar a que los demás procesos se lleven a cabo. Los procesos de soporte no crean directamente productos o servicios, pero son necesarios para facilitar o ayudar a la ejecución de los procesos operativos o de gestión.)", risk_manager_approval='T')
    #------------------
    # System Type
    #------------------
    db.system_type.update_or_insert((db.system_type.id==1), id=1, name="NA", description="NA", risk_manager_approval='T')
    db.system_type.update_or_insert((db.system_type.id==2), id=2, name="Operating System (Sistema Operativo)", description="", risk_manager_approval='T')
    db.system_type.update_or_insert((db.system_type.id==3), id=3, name="Data Base (Base de Datos)", description="", risk_manager_approval='T')
    db.system_type.update_or_insert((db.system_type.id==4), id=4, name="Application (Aplicacion)", description="Web applications, APIs, Web services", risk_manager_approval='T')
    db.system_type.update_or_insert((db.system_type.id==5), id=5, name="Network (Red)", description="Network components", risk_manager_approval='T')
    #------------------
    # Process
    #------------------
    db.process.update_or_insert((db.process.id==1), id=1, name="NA", description="NA", p_owner="NA", process_type_id=1, risk_manager_approval='T')
    db.process.update_or_insert((db.process.id==2), id=2, name="Marketing", description="", p_owner="processOwner", process_type_id=2, risk_manager_approval='T')
    db.process.update_or_insert((db.process.id==3), id=3, name="Process 1 (Proceso 1)", description="", p_owner="processOwner", process_type_id=2, risk_manager_approval='T')
    db.process.update_or_insert((db.process.id==4), id=4, name="Process 2 (Proceso 2)", description="", p_owner="processOwner", process_type_id=3, risk_manager_approval='T')
    db.process.update_or_insert((db.process.id==5), id=5, name="Process 3 (Proceso 3)", description="", p_owner="processOwner", process_type_id=4, risk_manager_approval='T')
    db.process.update_or_insert((db.process.id==6), id=6, name="Process 4 (Proceso 4)", description="", p_owner="processOwner", process_type_id=4, risk_manager_approval='T')
    #------------------
    # Maturity Level
    #------------------
    db.maturity_level.update_or_insert((db.maturity_level.id==1), id=1, name="Incomplete (Imcompleto)",   m_level=0, description="The process is not implemented or fails to achieve its process purpose. At this level, there is little or no evidence of any systematic achievement of the process purpose. (El proceso no se implementa o no logra su propósito. En este nivel, hay poca o ninguna evidencia de algún logro sistemático del propósito del proceso.)", risk_manager_approval='T')
    db.maturity_level.update_or_insert((db.maturity_level.id==2), id=2, name="Performed (Ejecutado)",     m_level=1, description="The implemented process achieves its process purpose. COBIT PAM 1 attribute. (El proceso implementado logra su propósito de proceso. COBIT PAM 1 atributo.)", risk_manager_approval='T')
    db.maturity_level.update_or_insert((db.maturity_level.id==3), id=3, name="Managed (Gestionado)",      m_level=2, description="The previously described performed process is now implemented in a managed fashion. Planned, monitored and adjusted. Its work products are appropriately established, controlled and maintained. COBIT PAM 2 attributes. (El proceso realizado descrito anteriormente se implementa ahora de manera administrada. Monitoreada, planificada y ajustada. Sus productos de trabajo se establecen, controlan y mantienen adecuadamente. COBIT PAM 2 atributos.)", risk_manager_approval='T')
    db.maturity_level.update_or_insert((db.maturity_level.id==4), id=4, name="Established (Establecido)", m_level=3, description="The previously described managed process is now implemented using a defined process that is capable of achieving its process outcomes. COBIT PAM 2 attributes. (El proceso gestionado descrito anteriormente ahora se implementa utilizando un proceso definido que es capaz de lograr los resultados del proceso. COBIT PAM 2 atributos.)", risk_manager_approval='T')
    db.maturity_level.update_or_insert((db.maturity_level.id==5), id=5, name="Predictable (Predecible)",  m_level=4, description="The previously described established process now operates within defined limits to achieve its process outcomes. COBIT PAM 2 attributes. (El proceso establecido descrito anteriormente ahora opera dentro de límites definidos para lograr los resultados del proceso. COBIT PAM 2 atributos.)", risk_manager_approval='T')
    db.maturity_level.update_or_insert((db.maturity_level.id==6), id=6, name="Optimazing (Optimizado)",   m_level=5, description="The previously described predictable process is continuously improved to meet relevant current and projected business goals. COBIT PAM 2 attributes. (El proceso predecible descrito anteriormente se mejora continuamente para cumplir con los objetivos comerciales actuales y proyectados relevantes. COBIT PAM 2 atributos.)", risk_manager_approval='T')
    #db.NivelMadurez.update_or_insert((db.NivelMadurez.id==7), id=7, Nombre="NA", Valor=0, Descripcion="Informativo", AprobacionJefeRiesgo='T')
    #---------------
    # Objetive Type
    #---------------
    db.objective_type.update_or_insert((db.objective_type.id==1), id=1, name="Operational (Operacional)", description="It refers to the effectiveness and efficiency of the organization's operations, including its performance, financial and operational objectives and the protection of its assets against any possible losses. (Garantizar operaciones efectivas y eficaces. Hacen referencia a la eficacia y eficiencia de las operaciones de la organización, incluidos sus objetivos de desempeño, financieros y operativos, y la protección de sus activos frente a posibles perdidas.)", risk_manager_approval='T')
    db.objective_type.update_or_insert((db.objective_type.id==2), id=2, name="Reporting (Información)",   description="To produce sufficient and reliable financial internal and external information in a transparent manner according to the concepts established by the regulators, organisms and/or by the own policies of the Company. (Generar información financiera y no financiera suficiente y confiable. Hacen referencia a la información financiera y no financiera interna y externa, y pueden abarcar aspectos de fiabilidad, oportunidad, transparencia u otros conceptos establecidos por los reguladores, organismos de normalización o por las políticas de la propia organización.)", risk_manager_approval='T')
    db.objective_type.update_or_insert((db.objective_type.id==3), id=3, name="Compliance (Cumplimiento)", description="It refers to the compliance of the laws and regulations to which the organization is subjected. (Cumplir con las regulaciones aplicables, tanto internas como externas. Hacen referencia al cumplimiento de las leyes y regulaciones a las que está sujeta la organización.)", risk_manager_approval='T')
    db.objective_type.update_or_insert((db.objective_type.id==4), id=4, name="Strategic (Estratégico)",   description="Senior management C-suite identifies the most important risks through the planning process and obtains Board approval. (Riesgos tanto para los objetivos estratégicos como de los objetivos estratégicos. La alta gerencia C-suite identifica los riesgos más importantes a través del proceso de planificación y obtiene aprobación de la Junta.)", risk_manager_approval='T')

    redirect(URL('default','grc_settings'))