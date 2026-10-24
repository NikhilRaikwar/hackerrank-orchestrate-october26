# Evaluation report

## Public samples

Sample answers are used only by this independent evaluator, never by inference.

| Metric | Result |
| --- | --- |
| status_accuracy | 100.0000% |
| exact_case_accuracy | 46.8750% |
| sequence_accuracy | 46.8750% |
| field_accuracy | 83.6219% |
| step_precision | 97.1751% |
| step_recall | 89.1192% |
| exact_step_precision | 71.7514% |
| step_f1 | 92.9730% |

Counts: `{"case_exact": 15, "cases": 32, "expected_steps": 193, "field_denominator": 1386, "fields_correct": 1159, "predicted_steps": 177, "sequence_exact": 15, "status_correct": 32, "step_exact_matches": 127, "step_identity_matches": 172}`

Confusion: `{"COMPLETE -> COMPLETE": 10, "INCOMPLETE -> INCOMPLETE": 22}`

Step precision/recall aligns by (phase, system, resource, operation). Exact step match includes numbering and citation. Field accuracy compares seven fields over the union of aligned step identities; missing/extra steps contribute seven errors. Sequence accuracy requires the complete ordered JSON array to match. Whole-case accuracy also requires matching status.

## Remaining public-sample differences

### case_03

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_03",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "step_no": 3,
      "phase": "VERIFICATION",
      "system_id": "analytics_platform",
      "resource_id": "analytics_9406",
      "operation": "VERIFY_RECORD_ANONYMIZED",
      "state": "ANONYMIZED",
      "evidence_id": "evidence_94"
    }
  ],
  "extra": [],
  "changed": []
}
```

### case_04

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_04",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "evidence_id": "evidence_54",
      "operation": "VERIFY_RECORD_ABSENT",
      "phase": "VERIFICATION",
      "resource_id": "account_004",
      "state": "ABSENT",
      "step_no": 1,
      "system_id": "account_service"
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "evidence_id": "evidence_56",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "phase": "VERIFICATION",
        "resource_id": "analytics_901",
        "state": "ANONYMIZED",
        "step_no": 2,
        "system_id": "analytics_platform"
      },
      "predicted": {
        "step_no": 1,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_901",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": "evidence_56"
      }
    }
  ]
}
```

### case_07

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_07",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [],
  "extra": [
    {
      "step_no": 3,
      "phase": "REMEDIATION",
      "system_id": "object_storage",
      "resource_id": "object_19",
      "operation": "DELETE_RECORD",
      "state": "ABSENT",
      "evidence_id": ""
    },
    {
      "step_no": 1,
      "phase": "FINDING",
      "system_id": "object_storage",
      "resource_id": "object_19",
      "operation": "REPORT_REMAINING_RECORD",
      "state": "PRESENT",
      "evidence_id": "evidence_46"
    },
    {
      "step_no": 6,
      "phase": "VERIFICATION",
      "system_id": "object_storage",
      "resource_id": "object_19",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    }
  ],
  "changed": [
    {
      "expected": {
        "evidence_id": "evidence_58",
        "operation": "REPORT_REMAINING_RECORD",
        "phase": "FINDING",
        "resource_id": "support_001",
        "state": "PRESENT",
        "step_no": 1,
        "system_id": "support_platform"
      },
      "predicted": {
        "step_no": 2,
        "phase": "FINDING",
        "system_id": "support_platform",
        "resource_id": "support_001",
        "operation": "REPORT_REMAINING_RECORD",
        "state": "PRESENT",
        "evidence_id": "evidence_58"
      }
    },
    {
      "expected": {
        "evidence_id": "",
        "operation": "DELETE_RECORD",
        "phase": "REMEDIATION",
        "resource_id": "support_001",
        "state": "ABSENT",
        "step_no": 2,
        "system_id": "support_platform"
      },
      "predicted": {
        "step_no": 4,
        "phase": "REMEDIATION",
        "system_id": "support_platform",
        "resource_id": "support_001",
        "operation": "DELETE_RECORD",
        "state": "ABSENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "evidence_id": "",
        "operation": "VERIFY_RECORD_ABSENT",
        "phase": "VERIFICATION",
        "resource_id": "support_001",
        "state": "ABSENT",
        "step_no": 4,
        "system_id": "support_platform"
      },
      "predicted": {
        "step_no": 7,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_001",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "evidence_id": "",
        "operation": "VERIFY_RECORD_ABSENT",
        "phase": "VERIFICATION",
        "resource_id": "account_007",
        "state": "ABSENT",
        "step_no": 3,
        "system_id": "account_service"
      },
      "predicted": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "account_service",
        "resource_id": "account_007",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_17

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_17",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [],
  "extra": [
    {
      "step_no": 4,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_6523",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    },
    {
      "step_no": 6,
      "phase": "VERIFICATION",
      "system_id": "identity_service",
      "resource_id": "tombstone_17",
      "operation": "VERIFY_RECORD_REDACTED",
      "state": "REDACTED",
      "evidence_id": ""
    }
  ],
  "changed": [
    {
      "expected": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_3245",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 7,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_3245",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 4,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_1797",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_1797",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_18

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_18",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [
    {
      "step_no": 9,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_5521",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    },
    {
      "step_no": 11,
      "phase": "VERIFICATION",
      "system_id": "security_service",
      "resource_id": "audit_record_6645",
      "operation": "VERIFY_RECORD_PRESENT",
      "state": "PRESENT",
      "evidence_id": ""
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 12,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_5569",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 10,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_5569",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 14,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_4890",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 12,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_4890",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 10,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_4013",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 9,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_4013",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 13,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_037",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 11,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_037",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_20

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_20",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [
    {
      "step_no": 7,
      "phase": "VERIFICATION",
      "system_id": "security_service",
      "resource_id": "audit_record_5569",
      "operation": "VERIFY_RECORD_PRESENT",
      "state": "PRESENT",
      "evidence_id": ""
    },
    {
      "step_no": 5,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_5037",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 8,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_1770",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_1770",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_4262",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_4262",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_21

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_21",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "step_no": 3,
      "phase": "VERIFICATION",
      "system_id": "analytics_platform",
      "resource_id": "analytics_5335",
      "operation": "VERIFY_RECORD_ANONYMIZED",
      "state": "ANONYMIZED",
      "evidence_id": "evidence_92"
    },
    {
      "step_no": 1,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_6440",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": "evidence_92"
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3737",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 1,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3737",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      }
    }
  ]
}
```

### case_22

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_22",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [
    {
      "step_no": 5,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_4990",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 7,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3482",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3482",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 8,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_4440",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 7,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_4440",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_8911",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_8911",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_23

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_23",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [
    {
      "step_no": 5,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_410",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 7,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_898",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_898",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "export_service",
        "resource_id": "export_7364",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "export_service",
        "resource_id": "export_7364",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 8,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_4128",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 7,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_4128",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_25

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_25",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "step_no": 1,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_3136",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": "evidence_92"
    },
    {
      "step_no": 3,
      "phase": "VERIFICATION",
      "system_id": "analytics_platform",
      "resource_id": "analytics_1895",
      "operation": "VERIFY_RECORD_ANONYMIZED",
      "state": "ANONYMIZED",
      "evidence_id": "evidence_92"
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_451",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 1,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_451",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      }
    }
  ]
}
```

### case_26

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_26",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "step_no": 4,
      "phase": "VERIFICATION",
      "system_id": "analytics_platform",
      "resource_id": "analytics_4566",
      "operation": "VERIFY_RECORD_ANONYMIZED",
      "state": "ANONYMIZED",
      "evidence_id": "evidence_92"
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_3120",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_3120",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": "evidence_92"
      }
    },
    {
      "expected": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_6244",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 4,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_6244",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": "evidence_92"
      }
    }
  ]
}
```

### case_27

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_27",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "step_no": 1,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_3866",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": "evidence_92"
    },
    {
      "step_no": 4,
      "phase": "VERIFICATION",
      "system_id": "analytics_platform",
      "resource_id": "analytics_4574",
      "operation": "VERIFY_RECORD_ANONYMIZED",
      "state": "ANONYMIZED",
      "evidence_id": "evidence_92"
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3830",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 1,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3830",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      }
    },
    {
      "expected": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_2295",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 3,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_2295",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": "evidence_92"
      }
    },
    {
      "expected": {
        "step_no": 3,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_4707",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_4707",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": "evidence_92"
      }
    },
    {
      "expected": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_5970",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 4,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_5970",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": "evidence_92"
      }
    }
  ]
}
```

### case_28

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_28",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "step_no": 1,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_5482",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": "evidence_92"
    },
    {
      "step_no": 4,
      "phase": "VERIFICATION",
      "system_id": "analytics_platform",
      "resource_id": "analytics_6077",
      "operation": "VERIFY_RECORD_ANONYMIZED",
      "state": "ANONYMIZED",
      "evidence_id": "evidence_92"
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 6,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_838",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 4,
        "phase": "VERIFICATION",
        "system_id": "backup_service",
        "resource_id": "backup_838",
        "operation": "VERIFY_RESTORE_BLOCKED",
        "state": "BLOCKED",
        "evidence_id": "evidence_92"
      }
    },
    {
      "expected": {
        "step_no": 3,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_2351",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_2351",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": "evidence_92"
      }
    },
    {
      "expected": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_2337",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 3,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_2337",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": "evidence_92"
      }
    },
    {
      "expected": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_9265",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      },
      "predicted": {
        "step_no": 1,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_9265",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_92"
      }
    }
  ]
}
```

### case_29

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_29",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [
    {
      "step_no": 9,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_7012",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 12,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_5281",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 11,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_5281",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 14,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_3827",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 13,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_3827",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 11,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3954",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 10,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_3954",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 13,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_5208",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 12,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_5208",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 10,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_1993",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 9,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_1993",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_30

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_30",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [
    {
      "step_no": 9,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_4163",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 11,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_1707",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 10,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_1707",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 13,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_3697",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 12,
        "phase": "VERIFICATION",
        "system_id": "analytics_platform",
        "resource_id": "analytics_3697",
        "operation": "VERIFY_RECORD_ANONYMIZED",
        "state": "ANONYMIZED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 12,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_6477",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 11,
        "phase": "VERIFICATION",
        "system_id": "support_platform",
        "resource_id": "support_6477",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 10,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_9359",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 9,
        "phase": "VERIFICATION",
        "system_id": "search_service",
        "resource_id": "search_9359",
        "operation": "VERIFY_RECORD_ABSENT",
        "state": "ABSENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 14,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_8524",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 13,
        "phase": "VERIFICATION",
        "system_id": "integration_service",
        "resource_id": "data_flow_8524",
        "operation": "VERIFY_DATA_FLOW_DISABLED",
        "state": "DISABLED",
        "evidence_id": ""
      }
    }
  ]
}
```

### case_31

Status: COMPLETE / expected COMPLETE

```text
{
  "case_id": "case_31",
  "expected_status": "COMPLETE",
  "predicted_status": "COMPLETE",
  "missing": [
    {
      "step_no": 1,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_4857",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": "evidence_51"
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_6909",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_51"
      },
      "predicted": {
        "step_no": 1,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_6909",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": "evidence_51"
      }
    },
    {
      "expected": {
        "step_no": 3,
        "phase": "VERIFICATION",
        "system_id": "identity_service",
        "resource_id": "tombstone_440",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": "evidence_51"
      },
      "predicted": {
        "step_no": 2,
        "phase": "VERIFICATION",
        "system_id": "identity_service",
        "resource_id": "tombstone_440",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": "evidence_51"
      }
    }
  ]
}
```

### case_32

Status: INCOMPLETE / expected INCOMPLETE

```text
{
  "case_id": "case_32",
  "expected_status": "INCOMPLETE",
  "predicted_status": "INCOMPLETE",
  "missing": [
    {
      "step_no": 3,
      "phase": "VERIFICATION",
      "system_id": "account_service",
      "resource_id": "account_8858",
      "operation": "VERIFY_RECORD_ABSENT",
      "state": "ABSENT",
      "evidence_id": ""
    }
  ],
  "extra": [],
  "changed": [
    {
      "expected": {
        "step_no": 4,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_7068",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 3,
        "phase": "VERIFICATION",
        "system_id": "security_service",
        "resource_id": "audit_record_7068",
        "operation": "VERIFY_RECORD_PRESENT",
        "state": "PRESENT",
        "evidence_id": ""
      }
    },
    {
      "expected": {
        "step_no": 5,
        "phase": "VERIFICATION",
        "system_id": "identity_service",
        "resource_id": "tombstone_9178",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      },
      "predicted": {
        "step_no": 4,
        "phase": "VERIFICATION",
        "system_id": "identity_service",
        "resource_id": "tombstone_9178",
        "operation": "VERIFY_RECORD_REDACTED",
        "state": "REDACTED",
        "evidence_id": ""
      }
    }
  ]
}
```


## Custom evaluation cases and results

All 11 synthetic behavioral tests passed with independently specified expected outcomes. Fixtures are generated in temporary directories; no real case IDs, sample labels, or corpus files are copied into them.

| Custom case | Expected behavior | Result |
| --- | --- | --- |
| Marketing opt-out, access request, or login help without erasure authorization | NOT_APPLICABLE and an empty step array | PASS |
| Primary absent while a regional replica remains present | INCOMPLETE and report/delete the remaining copy | PASS |
| New primary absence with an older replica still present | Do not assume the replica was cleaned; INCOMPLETE | PASS |
| Earlier email links a real copy; a similar email belongs to someone else | Include the historical copy and exclude the decoy | PASS |
| A deletion observation occurs after the audit cutoff | Keep the earlier INCOMPLETE verdict | PASS |
| Tombstone contains only a permitted reference and security record remains | COMPLETE; verify redaction and retention without deleting either | PASS |
| Tombstone retains an identifying hash | Report PII, redact, and verify | PASS |
| Active connector, unsafe backup restore and present account | Disable flow, block restore, then delete record | PASS |
| Input facts are reordered and an unrelated person is added | Prediction remains identical | PASS |
| Later sync recreates an earlier deleted record | INCOMPLETE | PASS |
| An absence snapshot covers a different subject cohort | It cannot prove this subject's deletion | PASS |

Reproduce with `python -m unittest discover -s code/evaluation -p test_cases.py -v`.

## Failures found and improvements made

Initial structured-only evaluation left several cases unresolved because media was omitted. Added PDF interpretation and screenshot vision. A first vision pass confused user/ticket/business references with logical resource IDs and misclassified some business rows; added faithful transcription, literal-reference validation, catalog joins, and rejection of invented resource IDs. Added handlers for nested exports, escaped cloud logs, bracket/pipe/syslog formats, trace correlation, export metadata readbacks and denied restore authorization. Retained hashes and stable references are evaluated differently for tombstones and analytics. Added scoped negative queries and stronger proof selection instead of trusting operation SUCCESS. Tightened temporal linkage to ten minutes with an alternative-candidate margin to reduce false resource assignments. Added a regression test ensuring a newer primary lookup cannot silently clear a retained replica copy.

## Remaining limitations

All 32 public deletion statuses match, but only 15 complete ordered outputs match exactly. The report above enumerates every mismatch rather than hiding citation, resource coverage, or sequence errors behind the status score. Most remaining differences concern verification coverage for de-identified resources whose subject links are missing/ambiguous, extra grounded resources, and evidence selection. The system does not fill those gaps from sample answers or numeric case/resource patterns.

Temporal report/operation correlation is probabilistic and appears in diagnostics; it is not a proof of record ownership. A bundled historical observation uses its contained observation/capture time, while standalone artifacts use their capture time; the supplied exported-at versus inner-snapshot timestamps require this explicit interpretation. Conditional retention outside the supplied conditions and absent policy-required retained records can require review; the allowed operation enum has no reconstruction action for a missing retained record. No organizer-only truth, private labels, or hidden scoring feedback was used. Public samples contain no NOT_APPLICABLE example, so that behavior is covered by custom tests and model intent classification rather than a claimed public-label accuracy.

## Full run and validation

The final normal-mode run generated exactly 518 sorted prediction rows, with no unresolved audits and no extraction errors. All 94 manifested artifacts were processed, including all local images and PDFs. Step schema, enum/state compatibility, evidence ID existence, phase/operation/system/resource ordering, consecutive numbering, duplicate prevention, and status-specific citation requirements passed validation. Token/cost accounting is in the separate required usage report. Hidden-test accuracy and leaderboard rank are unknown.
