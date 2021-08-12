# -*- coding: utf-8 -*-

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),

    (T('Risk Catalog'), False, '#', [        
        #LI(_class="divider"),
        (T('Risk Classification'), False, URL('default', 'risk_classification')),
        (T('Risk Treatment'), False, URL('default', 'risk_treatment')),
        (T('Impact Level'), False, URL('default', 'impact_level')),
        (T('Probability Level'), False, URL('default', 'probability_level')),
    ]),

    (T('Organization Context'), False, '#', [    
        (T('Department'), False, URL('default', 'department')),
        (T('Objective Type'), False, URL('default', 'objective_type')),
        (T('Company'), False, URL('default', 'company')),
        (T('Company Objetive'), False, URL('default', 'company_objective')),
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

