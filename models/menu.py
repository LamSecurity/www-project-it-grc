# -*- coding: utf-8 -*-

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),

    (T('Risk Catalog'), False, '#', [        
        #LI(_class="divider"),
        (T('Risk Classification'), False, URL('default', 'risk_classification')),
        (T('Risk Treatment'), False, URL('default', 'risk_treatment')),
        #(T('Risk Factor Group'), False, URL('default', 'GrupoFactorRiesgo')),
        #LI(_class="divider"),
        #(T('Control Clasification'), False, URL('default', 'ClasificacionControl')),
        #(T('Control Type'), False, URL('default', 'TipoControl')),
        #(T('Control Group'), False, URL('default', 'GrupoControl')),
        #(T('Objetive Type'), False, URL('default', 'TipoObjetivo')),
        #LI(_class="divider"),
        #LI(_class="divider"),
        #(T('Region'), False, URL('default', 'Region')),
        #(T('Department'), False, URL('default', 'Direccion')),
        #(T('Policy Catalog'), False, URL('default', 'CatalogoPolitica')),
        #(T('Policy Statement'), False, URL('default', 'DetallePolitica')),
    ]),

    (T('Organization Context'), False, '#', [    
        (T('Department'), False, URL('default', 'department')),
        (T('Objective Type'), False, URL('default', 'objective_type')),
    ]),

    (T('Asset'), False, '#', [    
        (T('Process Type'), False, URL('default', 'process_type')),
        (T('System Type'), False, URL('default', 'system_type')),
        (T('Process'), False, URL('default', 'process')),
    ]),

    (T('Audit & Control'), False, '#', [    
        (T('Maturity Level'), False, URL('default', 'maturity_level')),
    ]),

    (T('Project'), False, '#', [    
        #(T('Maturity Level'), False, URL('default', 'maturity_level')),
    ]),

    (T('Tool'), False, '#', [    
        #(T('Maturity Level'), False, URL('default', 'maturity_level')),
    ]),

    (T('Admin'), False, '#', [    
        (T('Settings'), False, URL('default', 'grc_settings')),
    ]),
]

