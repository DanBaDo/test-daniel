from datetime import datetime
from itertools import accumulate

import requests
from django_mock_queries.query import MockSet, MockModel

from aux.errors_handling import errorLogger
from fake_solar_api.defines import ENDPOINTS, SG_IDS, RESP_STATUS, Response

def request(endpoint):
    '''
    Generic FakeSolar API request
        endpoin - URL label in ENDPOINTS dictionary.
        returns -> Response
        Example: 
            data = request(ENDPOINTS["INSPECTORS"])
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
        Example:
            ids = our_ids_in_integrations(SG_IDS, inspector.availableIntegrations)
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
        Example:
            sg_inspectors = solar_grade_inspectors(
                request(ENDPOINTS["INSPECTORS"]),
                SG_IDS,
                "availableIntegrations"
            )
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
        Example:
            sg_inspections = solar_grade_inspections(
                sg_inspectors,
                request(ENDPOINTS["INSPECTIONS"]),
                "availableIntegrations"
            )
    '''
    inspectors_by_id = {}
    inspections = []

    try:
        for inspector in sg_inspectors:
            inspectors_by_id[inspector.id] = inspector

        for inspection in inspections:
            if inspection.inspectorId in inspectors_by_id.keys():
                date = datetime.strptime(inspection.createdAt[0:10], "%Y-%m-%d")
                inspection = {
                    "title": f'{inspection.city} - {date.strftime("%Y")}/{date.strftime("%m")}',
                    "inspectorName": inspector[inspection.inspectorId]["name"],
                    "itemsOk": accumulate([
                        1 for inspection in inspections
                        if inspection.isIssue == False
                    ]),
                    "issuesWarningCount": accumulate([
                        1 for inspection in inspections
                        if inspection.isIssue == True and inspection.severity < 60
                    ]),
                    "issuesCriticalCount": accumulate([
                        1 for inspection in inspections
                        if inspection.isIssue == True and inspection.severity >= 60
                    ]),
                    "Company": "SolarGrade",
                }
                inspections.append(inspection)
        return inspections
    except Exception as error:
        errorLogger(error, __name__, "solar_grade_inspectors")
        return []

def fake_solar_query_set_factory(inspections):
    '''
    Return a mocked model from inspections list
    inspections - solar_grade_inspections generated inspections list
    returns -> QuerySet
    Example:
        fs_query = fake_solar_query_set_factory(sg_inspections)
    '''
    mock_inspections = [ 
        MockModel(**item)
        for item in inspections
    ]
    fs_model = MockSet(mock_inspections)
    return fs_model


# TESTS
sg_inspectors = solar_grade_inspectors(
            request(ENDPOINTS["INSPECTORS"]),
            SG_IDS,
            "availableIntegrations"
        )

print(sg_inspectors)

sg_inspections = solar_grade_inspections(
    sg_inspectors,
    request(ENDPOINTS["INSPECTIONS"]),
    "availableIntegrations"
)

print(sg_inspections)

fs_query = fake_solar_query_set_factory(sg_inspections)

print(fs_query)