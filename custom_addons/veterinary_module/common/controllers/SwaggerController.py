from odoo import http
from odoo.http import request

class SwaggerController(http.Controller):

    @http.route('/api/docs/swagger.json', type='json', auth='none', methods=['GET'], csrf=False)
    def swagger_json(self):
        return {
            "openapi": "3.0.0",
            "info": {
                "title": "Veterinary API",
                "version": "1.0.0",
                "description": "Swagger API for Veterinary Module (Animal, Diagnosis, Treatment, Medical, DiagnosisType, AnimalSort)",
            },
            "paths": {
                "/api/animals": {
                    "get": {
                        "summary": "Get list of Animals",
                        "responses": {
                            "200": {
                                "description": "List of animals"
                            }
                        }
                    },
                    "post": {
                        "summary": "Create a new Animal",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "animal_name": {"type": "string"},
                                            "birth_date": {"type": "string", "format": "date-time"},
                                            "patient_number": {"type": "string"},
                                            "sterilised": {"type": "boolean"},
                                            "sort": {"type": "object"},
                                            "diagnoses": {
                                                "type": "array",
                                                "items": {"type": "object"}
                                            }
                                        },
                                        "required": ["animal_name", "birth_date"]
                                    }
                                }
                            }
                        },
                        "responses": {
                            "201": {"description": "Animal created successfully"}
                        }
                    }
                },
                "/api/animal_sorts": {
                    "get": {"summary": "Get list of AnimalSorts"},
                    "post": {
                        "summary": "Create AnimalSort",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "sort_name": {"type": "string"},
                                        },
                                        "required": ["sort_name"]
                                    }
                                }
                            }
                        },
                        "responses": {
                            "201": {"description": "AnimalSort created successfully"}
                        }
                    }
                },
                "/api/diagnosis_types": {
                    "get": {"summary": "Get list of DiagnosisTypes"},
                    "post": {
                        "summary": "Create DiagnosisType",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "sort_name": {"type": "string"},
                                            "description": {"type": "string"}
                                        },
                                        "required": ["sort_name"]
                                    }
                                }
                            }
                        }
                    }
                },
                "/api/treatments": {
                    "get": {"summary": "Get list of Treatments"},
                    "post": {
                        "summary": "Create Treatment",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "date_time": {"type": "string", "format": "date-time"},
                                            "realised": {"type": "boolean"},
                                            "description": {"type": "string"},
                                            "medicals": {
                                                "type": "array",
                                                "items": {"type": "object"}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "/api/medicals": {
                    "get": {"summary": "Get list of Medicals"},
                    "post": {
                        "summary": "Create Medical",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "date_time": {"type": "string", "format": "date-time"},
                                            "name": {"type": "string"},
                                            "description": {"type": "string"},
                                            "treatment_ids": {
                                                "type": "array",
                                                "items": {"type": "object"}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "/api/diagnoses": {
                    "get": {"summary": "Get list of Diagnoses"},
                    "post": {
                        "summary": "Create Diagnosis",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "date_time": {"type": "string", "format": "date-time"},
                                            "cured": {"type": "boolean"},
                                            "description": {"type": "string"},
                                            "type": {"type": "object"},
                                            "treatments": {"type": "object"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
            }
        }
