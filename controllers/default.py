# -*- coding: utf-8 -*-
import base64

def index():
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

#--------------
#Risk Catalog
#--------------
@auth.requires_login()
def risk_classification():
    db.risk_classification.id.readable=False
    db.risk_classification.risk_manager_approval.writable=False
    db.risk_classification.risk_analyst_approval.writable=False
    db.risk_classification.risk_manager_log.writable=False
    db.risk_classification.risk_analyst_log.writable=False
    table_name = 'risk_classification'
    fields = (db.risk_classification.name, db.risk_classification.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.risk_classification, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.risk_classification, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.risk_classification.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

@auth.requires_login()
def risk_treatment():
    db.risk_treatment.id.readable=False
    db.risk_treatment.risk_manager_approval.writable=False
    db.risk_treatment.risk_analyst_approval.writable=False
    db.risk_treatment.risk_manager_log.writable=False
    db.risk_treatment.risk_analyst_log.writable=False
    table_name = 'risk_treatment'
    fields = (db.risk_treatment.name, db.risk_treatment.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.risk_treatment, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.risk_treatment, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.risk_treatment.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

#---------------------
#Organization Context
#---------------------
@auth.requires_login()
def department():
    db.department.id.readable=False
    db.department.risk_manager_approval.writable=False
    db.department.risk_analyst_approval.writable=False
    db.department.risk_manager_log.writable=False
    db.department.risk_analyst_log.writable=False
    table_name = 'department'
    fields = (db.department.name, db.department.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.department, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.department, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.department.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

@auth.requires_login()
def objective_type():
    db.objective_type.id.readable=False
    db.objective_type.risk_manager_approval.writable=False
    db.objective_type.risk_analyst_approval.writable=False
    db.objective_type.risk_manager_log.writable=False
    db.objective_type.risk_analyst_log.writable=False
    table_name = 'objective_type'
    fields = (db.objective_type.name, db.objective_type.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.objective_type, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.objective_type, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.objective_type.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

#--------------------------------------
#Assets (IT systems, processes, data)
#--------------------------------------
@auth.requires_login()
def process_type():
    db.process_type.id.readable=False
    db.process_type.risk_manager_approval.writable=False
    db.process_type.risk_analyst_approval.writable=False
    db.process_type.risk_manager_log.writable=False
    db.process_type.risk_analyst_log.writable=False
    table_name = 'process_type'
    fields = (db.process_type.name, db.process_type.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.process_type, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.process_type, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.process_type.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

@auth.requires_login()
def system_type():
    db.system_type.id.readable=False
    db.system_type.risk_manager_approval.writable=False
    db.system_type.risk_analyst_approval.writable=False
    db.system_type.risk_manager_log.writable=False
    db.system_type.risk_analyst_log.writable=False
    table_name = 'system_type'
    fields = (db.system_type.name, db.system_type.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.system_type, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.system_type, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.system_type.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

@auth.requires_login()
def process():
    db.process.id.readable=False
    db.process.risk_manager_approval.writable=False
    db.process.risk_analyst_approval.writable=False
    db.process.risk_manager_log.writable=False
    db.process.risk_analyst_log.writable=False
    table_name = 'process'
    fields = (db.process.name, db.process.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.process, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.process, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.process.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

#------------------------
#Audit & Control
#------------------------
@auth.requires_login()
def maturity_level():
    db.maturity_level.id.readable=False
    db.maturity_level.risk_manager_approval.writable=False
    db.maturity_level.risk_analyst_approval.writable=False
    db.maturity_level.risk_manager_log.writable=False
    db.maturity_level.risk_analyst_log.writable=False
    table_name = 'maturity_level'
    fields = (db.maturity_level.name, db.maturity_level.description)
    if request.vars.get('keywords'):
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved', base64.b64encode(request.vars.get('keywords'))] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved', base64.b64encode(request.vars.get('keywords'))]))]
    else:
        links = [lambda row: A(T('Approve'),_class='button btn btn-success',_href=URL("default","_log_update", args=[row.id, table_name, "1", 'Approved'] )), lambda row: A(T('Not Approved'),_class='button btn btn-primary',_href=URL("default","_log_update", args=[row.id, table_name, "0", 'Not Approved']))]
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.maturity_level, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=True, user_signature=True, paginate=10, maxtextlength=500))
    elif auth.has_membership(role='riskAnalyst'):
        _aproval_update(table_name)
        return dict(form=SQLFORM.grid(db.maturity_level, fields=fields, links=links, searchable=True, create=True, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    elif  auth.has_membership(role='riskOwner') or auth.has_membership(role='auditManager') or auth.has_membership(role='auditAnalyst') or auth.has_membership(role='guest'):
        query = db.maturity_level.risk_manager_approval=='T'
        return dict(form=SQLFORM.grid(query=query, fields=fields, searchable=True, create=False, deletable=False,editable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))


#-----------------------------------
#To set basic configurations in GRC
#-----------------------------------
@auth.requires_login()
def grc_settings():
    if auth.has_membership(role='admin') or auth.has_membership(role='riskManager'):
        links = [lambda row: A(T('Load Demo Data'),_class='button btn btn-warning',_href=URL("grc_demo_data","_load_demo_data")) ]
        return dict(form=SQLFORM.grid(db.grc_settings, links=links, searchable=True, create=False, editable=True, deletable=False, user_signature=True, paginate=10, maxtextlength=500))
    else:
        redirect(URL('default','index'))

#-----------------------------------------------------------------------
#Function to update approval status to False if the record is edited
#-----------------------------------------------------------------------
@auth.requires_login()
def _aproval_update(table_name):

    if request.args(0) == 'edit':
        if table_name=='risk_classification':
            db(db.risk_classification.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.risk_classification.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')            
        if table_name=='risk_treatment':
            db(db.risk_treatment.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.risk_treatment.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')
        if table_name=='department':
            db(db.department.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.department.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')
        if table_name=='process_type':
            db(db.process_type.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.process_type.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')
        if table_name=='system_type':
            db(db.system_type.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.system_type.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')
        if table_name=='process':
            db(db.process.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.process.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')
        if table_name=='maturity_level':
            db(db.maturity_level.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.maturity_level.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')
        if table_name=='objective_type':
            db(db.objective_type.id==request.args[len(request.args)-1]).update(risk_analyst_approval='F')
            db(db.objective_type.id==request.args[len(request.args)-1]).update(risk_manager_approval='F')
    
        redirect(URL("default","_log_update", args=[request.args[len(request.args)-1], table_name, '0', 'Edit']))


#---------------------------------------------------------------------------
#Function to update approval status to False(0)/True(1) and log this action
#---------------------------------------------------------------------------
@auth.requires_login()
def _log_update():
    #---------------------------------------------
    #If username or email configuration in db.py
    #---------------------------------------------
    action = request.args(3)
    has_context_params = False

    try:
        signature = action + ',' + auth.user.username + ',' + request.client + ',' + str(request.now) #+ ',' + str(response.session_id)
    except:
        signature = action + ',' + auth.user.email + ',' + request.client + ',' + str(request.now)    #+ ',' + str(response.session_id)
      
    #-----------------------------------------------
    #context_params is to use the same http context 
    #-----------------------------------------------
    if request.args(4):
        context_params = base64.b64decode(request.args(4))
        has_context_params = True
    else:
        pass

    if request.args(1) == 'risk_classification':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.risk_classification.id==request.args(0)).update(risk_manager_log=signature)
                db(db.risk_classification.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.risk_classification.id==request.args(0)).update(risk_manager_log=signature)
                db(db.risk_classification.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.risk_classification.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.risk_classification.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.risk_classification.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.risk_classification.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('risk_classification', vars=dict(keywords=context_params)))
        else:
            redirect(URL('risk_classification'))

    if request.args(1) == 'risk_treatment':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.risk_treatment.id==request.args(0)).update(risk_manager_log=signature)
                db(db.risk_treatment.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.risk_treatment.id==request.args(0)).update(risk_manager_log=signature)
                db(db.risk_treatment.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.risk_treatment.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.risk_treatment.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.risk_treatment.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.risk_treatment.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('risk_treatment', vars=dict(keywords=context_params)))
        else:
            redirect(URL('risk_treatment'))
            
    if request.args(1) == 'department':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.department.id==request.args(0)).update(risk_manager_log=signature)
                db(db.department.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.department.id==request.args(0)).update(risk_manager_log=signature)
                db(db.department.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.department.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.department.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.department.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.department.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('department', vars=dict(keywords=context_params)))
        else:
            redirect(URL('department'))

    if request.args(1) == 'process_type':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.process_type.id==request.args(0)).update(risk_manager_log=signature)
                db(db.process_type.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.process_type.id==request.args(0)).update(risk_manager_log=signature)
                db(db.process_type.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.process_type.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.process_type.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.process_type.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.process_type.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('process_type', vars=dict(keywords=context_params)))
        else:
            redirect(URL('process_type'))

    if request.args(1) == 'system_type':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.system_type.id==request.args(0)).update(risk_manager_log=signature)
                db(db.system_type.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.system_type.id==request.args(0)).update(risk_manager_log=signature)
                db(db.system_type.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.system_type.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.system_type.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.system_type.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.system_type.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('system_type', vars=dict(keywords=context_params)))
        else:
            redirect(URL('system_type'))

    if request.args(1) == 'process':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.process.id==request.args(0)).update(risk_manager_log=signature)
                db(db.process.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.process.id==request.args(0)).update(risk_manager_log=signature)
                db(db.process.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.process.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.process.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.process.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.process.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('process', vars=dict(keywords=context_params)))
        else:
            redirect(URL('process'))

    if request.args(1) == 'maturity_level':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.maturity_level.id==request.args(0)).update(risk_manager_log=signature)
                db(db.maturity_level.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.maturity_level.id==request.args(0)).update(risk_manager_log=signature)
                db(db.maturity_level.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.maturity_level.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.maturity_level.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.maturity_level.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.maturity_level.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('maturity_level', vars=dict(keywords=context_params)))
        else:
            redirect(URL('maturity_level'))

    if request.args(1) == 'objective_type':
        if (auth.has_membership(role='riskManager') or auth.has_membership(role='admin')):
            if request.args(2)=='1':
                db(db.objective_type.id==request.args(0)).update(risk_manager_log=signature)
                db(db.objective_type.id==request.args(0)).update(risk_manager_approval='T')
            elif request.args(2)=='0':
                db(db.objective_type.id==request.args(0)).update(risk_manager_log=signature)
                db(db.objective_type.id==request.args(0)).update(risk_manager_approval='F')
        elif (auth.has_membership(role='riskAnalyst')):
            if request.args(2)=='1':
                db(db.objective_type.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.objective_type.id==request.args(0)).update(risk_analyst_approval='T')
            elif request.args(2)=='0':
                db(db.objective_type.id==request.args(0)).update(risk_analyst_log=signature)
                db(db.objective_type.id==request.args(0)).update(risk_analyst_approval='F')
        if has_context_params:
            redirect(URL('objective_type', vars=dict(keywords=context_params)))
        else:
            redirect(URL('objective_type'))