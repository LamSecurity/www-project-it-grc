# -*- coding: utf-8 -*-

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),

    (T('Catalog'), False, '#', [        
        #LI(_class="divider"),
        (T('Risk Classification'), False, URL('default', 'risk_classification')),
        (T('Risk Treatment'), False, URL('default', 'risk_treatment')),
        (T('Impact Level'), False, URL('default', 'impact_level')),
        (T('Probability Level'), False, URL('default', 'probability_level')),
        (T('Risk Level'), False, URL('default', 'risk_level')),
    ]),

    (T('Context'), False, '#', [    
        (T('Department'), False, URL('default', 'department')),
        (T('Objective Type'), False, URL('default', 'objective_type')),
        (T('Company'), False, URL('default', 'company')),
        (T('Company Objetive'), False, URL('default', 'company_objective')),
    ]),

    (T('Asset'), False, '#', [    
        (T('Process Type'), False, URL('default', 'process_type')),
        (T('System Type'), False, URL('default', 'system_type')),
        (T('Process'), False, URL('default', 'process')),
        (T('System'), False, URL('default', 'system_asset')),
    ]),

    (T('Risk'), False, '#', [    
        (T('Risk Analysis'), False, URL('default', 'strategic_risk_analysis')),
        (T('Risk Analysis & Classification'), False, URL('default', 'risk_analysis_classification')),
        (T('Risk Analysis & Objective'), False, URL('default', 'risk_analysis_objective')),
    ]),

    (T('Audit'), False, '#', [    
        (T('Maturity Level'), False, URL('default', 'maturity_level')),
        (T('Benchmark'), False, URL('default', 'benchmark')),
        (T('Benchmark Control Objective'), False, URL('default', 'bench_control_objective')),
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
