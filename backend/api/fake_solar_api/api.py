import requests
from aux.errors_handling import errorLogger

from django_mock_queries import MockSet, MockModel

from fake_solar_api.defines import ENDPOINTS, SG_IDS, RESP_STATUS, Response

def request(endpoint):
    '''
    Generic FakeSolar API request
        endpoin - URL label in ENDPOINTS dictionary.
        returns -> Response
    '''
    try:
        if endpoint in ENDPOINTS:
            return Response(
                RESP_STATUS["OK"],
                requests.get(ENDPOINTS[endpoint]).json(),
            )
    except Exception as error:
        errorLogger(error, __name__, "request")
        return Response(
            RESP_STATUS["ERROR"],
            [],
            error
        )

def our_ids_in_integrations(ids, integrations):
    '''
    Auxiliar function for verifiying if any of ours IDs are in
    inspector API integrations list.
        ids - Our IDs set.
        integrations - inspector API integrations list.
        returns -> Boolean.
    '''
    try:
        return len( set(ids).intersection(integrations) ) == True
    except Exception as error:
        errorLogger(error, __name__, "ids_in_integrations")
        return False

def solar_grade_inspectors(inspectors, sg_ids, integrations_field):
    '''
    Returns SolarGrade inspectors from inspectors list
        inspectors - Inspectors list.
        sg_ids - SolarGrade IDs list.
        integrations_field - Inspector integrations list field.
        returns -> []
    '''
    try: 
        return [
            inspector for inspector in inspectors
            if our_ids_in_integrations(sg_ids, inspector[integrations_field])
        ]
    except Exception as error:
        errorLogger(error, __name__, "solar_grade_inspectors")
        return []

def solar_grade_inspections(sg_inspectors, inspections, inspector_id_field):
    '''
    Returns SolarGrade inspectors inspections from inspections list.
        sg_inspectos - SolarGrade inspectors list.
        inspections - Inspections list.
        inspector_id_field - Inspection inspector ID field.
        returns -> []
    '''
    try:
        sg_inspectors_ids = set(
            [ inspector["id"] for inspector in sg_inspectors ]
        )
        return [
            inspection for inspection in inspections
            if inspection[inspector_id_field] in sg_inspectors_ids
        ]
    except Exception as error:
        errorLogger(error, __name__, "solar_grade_inspectors")
        return []

def fake_solar_query_set_factory(inspections):
    mock_inspections = [ 
        MockModel(
            title = "TODO", #TODO: Get data for title
            inspectorName = "TODO", #TODO: Get inspection name
            itemsOk = "TODO", #TODO: Get total ok items
            issuesWarningCount = "TODO", #TODO: Get total warning items
            issuesCriticalCount= "TODO", #TODO: Get total critial items
            Company = "SolarGrade"
        )
        for item in inspections
    ]
    fs_model = MockSet(mock_inspections)
    return fs_model

