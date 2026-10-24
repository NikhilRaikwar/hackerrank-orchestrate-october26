# Complete source-file inspection

Generated from local tracked files; sample answers are validation data only.

## AGENTS.md

Bytes: 23547; SHA-256: 559446bcb3cebbedae90deb0931545b10ca5469266acde856b7cc7a011f09afe

Lines: 422

## CLAUDE.md

Bytes: 11; SHA-256: 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49

Lines: 1

## README.md

Bytes: 8386; SHA-256: 9f88c1c852a2ec94461775bf7a4f1ab6d6cfebd98e4031d961ef8b8146389c20

Lines: 157

## agent_trace_instructions.md

Bytes: 8163; SHA-256: 51acd5ed499c3071e7987c1f8a17d6dd643afd1e5fdab4da8a024ea7bc5f63a5

Lines: 130

## code/evaluation/main.py

Bytes: 0; SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Lines: 0

## code/main.py

Bytes: 0; SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Lines: 0

## dataset/deletion_requests.csv

Bytes: 163664; SHA-256: 78464850941b84baecf9fee586208752521c4521d0c15c76f741516eb7f700d2

Rows: 518

Fields: case_id, email, requested_at, reported_status, reported_at, audit_at, request_text

Audit range: 2026-01-29T12:00:00Z to 2026-10-01T12:00:00Z

## dataset/deletion_rules.csv

Bytes: 1039; SHA-256: e12d47ca4cbecc4a3c924b52705d9c5b1ebcfa71d6a28f58d988571eeccb32f7

Rows: 15

Fields: rule_id, data_category, condition, required_action

## dataset/evidence/databases/customer_accounts_failover_replica_20260902.sql

Bytes: 2052; SHA-256: 0435cf6d1b6527f4cd8f5b2e93605a8ff32410503594e89e461b48d562fd7546

Table customer_profiles_failover_replica: 4 rows; fields: resource_id, user_id, full_name, email, phone, account_status, updated_at

Table customer_profiles_primary: 3 rows; fields: resource_id, user_id, full_name, email, phone, account_status, updated_at

## dataset/evidence/databases/customer_data_failover_replica_20260920.sql

Bytes: 12250; SHA-256: 457a0164d6f6e3a38f9d13a977a2fc283d4ac2ad08e4f8cd6c90bfd76065a772

Table customer_data_failover_replica: 16 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_primary: 16 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_inventory_20260213.sql

Bytes: 5436; SHA-256: 67fdcb0f5edc1b5abf8851237cfcb45abcf475f1d765db4e0dc2547903475349

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 1 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 3 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 0 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 2 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 4 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 4 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 7 rows; fields: origin_system, captured_at

Table support_records: 2 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260310.sql

Bytes: 6545; SHA-256: 0f64bf5ccfddc50264b6794bec399448eeb51a3becfd603e68b6189d046abbb0

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 4 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 5 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 0 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 7 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 2 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 8 rows; fields: origin_system, captured_at

Table support_records: 3 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260404.sql

Bytes: 5721; SHA-256: cc07a4436bc03cda52885cedd72a1c76175bc9972db9d6dbc043a0590c176e40

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 2 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 4 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 0 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 5 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 3 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 8 rows; fields: origin_system, captured_at

Table support_records: 2 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260504.sql

Bytes: 6084; SHA-256: 2d92e3c24e394f5125882e1b50d3fb0d8edd9b8e6c8427fd66cd6d1baa28d045

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 4 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 3 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 0 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 1 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 6 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 3 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 7 rows; fields: origin_system, captured_at

Table support_records: 3 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260524.sql

Bytes: 6601; SHA-256: 78bf874047cfa92f2b5328395e26144481a7809cd9dd3ec3d1f43445a89c5dac

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 4 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 6 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 0 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 5 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 4 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 8 rows; fields: origin_system, captured_at

Table support_records: 3 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260618.sql

Bytes: 5787; SHA-256: 558fd7f00790c18907bdbc7e8cbedc3437aff5060bf8e862b8239d81102d8634

Table backup_restore_entries: 0 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 1 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 4 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 2 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 6 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 2 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 7 rows; fields: origin_system, captured_at

Table support_records: 3 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260703.sql

Bytes: 6626; SHA-256: 897e523d73eb5c69f5c88d4b8be14419f229a35e3a4bdd21086071e25e348371

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 2 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 5 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 0 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 5 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 5 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 8 rows; fields: origin_system, captured_at

Table support_records: 5 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260723.sql

Bytes: 6994; SHA-256: 073b6313dd8cb46aa73b6f49d4fb020076b14afdc973e24372394bbc03a52646

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 4 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 5 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 1 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 7 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 2 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 8 rows; fields: origin_system, captured_at

Table support_records: 5 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260817.sql

Bytes: 5922; SHA-256: ab967e983129d9af9e08503103cec293f35e7c1bf097e551002d0df45c5ae066

Table backup_restore_entries: 1 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 1 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 4 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 1 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 5 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 2 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 8 rows; fields: origin_system, captured_at

Table support_records: 4 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260905.sql

Bytes: 2314; SHA-256: f2c98db0e2806b66e57ef9bc72303aaabd8f26674d41a5f0f04114a74d7f1e0c

Table backup_restore_entries: 0 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 0 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 0 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 0 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 0 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 0 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 0 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 1 rows; fields: origin_system, captured_at

Table support_records: 0 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_inventory_20260916.sql

Bytes: 5550; SHA-256: 4e16a1b0ee094817f902074d766b5dcbe5e683ef0a8524f9b3761f5be658a127

Table backup_restore_entries: 2 rows; fields: resource_id, customer_reference, customer_email, archive_key, restore_allowed, updated_at

Table connector_subscriptions: 2 rows; fields: resource_id, customer_reference, customer_email, connector_name, enabled, last_delivery_status, updated_at

Table customer_analytics_profiles: 2 rows; fields: resource_id, customer_reference, email, phone, email_hash, audience_cohort, updated_at

Table customer_exports: 1 rows; fields: resource_id, customer_reference, owner_email, owner_phone, object_key, updated_at

Table customer_profiles: 1 rows; fields: resource_id, customer_reference, full_name, email, phone, email_hash, account_status, updated_at

Table customer_search_documents: 3 rows; fields: resource_id, customer_reference, display_name, email, phone, email_hash, index_name, updated_at

Table security_audit_records: 3 rows; fields: resource_id, subject_reference, event_code, retention_until, updated_at

Table snapshot_scope: 8 rows; fields: origin_system, captured_at

Table support_records: 3 rows; fields: resource_id, customer_reference, requester_name, requester_email, requester_phone, message_excerpt, updated_at

## dataset/evidence/databases/customer_data_read_replica_20260613.sql

Bytes: 19611; SHA-256: 51cef77ebba6e9af1e3dba901ad8685a9b6cf0e746d5adf15db70d0f768f78dc

Table customer_data_primary: 24 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_read_replica: 26 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_read_replica_20260708.sql

Bytes: 23547; SHA-256: 462002cab8801ee51227724627e7cd941687e1a65eae9bdc249910bed68443da

Table customer_data_primary: 31 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_read_replica: 32 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_read_replica_20260802.sql

Bytes: 19312; SHA-256: c1363207e80b1b4ee3f5cceca032ee9b3da6c54337801e247ea3eb9132d9872a

Table customer_data_primary: 24 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_read_replica: 25 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_read_replica_20260827.sql

Bytes: 23576; SHA-256: 519c2026b317ef65c7992fcf341e17ce1da0eee85448f18a64ed23cf6a78a068

Table customer_data_primary: 29 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_read_replica: 30 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_read_replica_20260921.sql

Bytes: 24657; SHA-256: c614fa6f225e0527bc3a888d52f0e2b12df31e5b7d1f3aed43f7102c1e442e89

Table customer_data_primary: 30 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_read_replica: 31 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_regional_replicas_20260330.sql

Bytes: 35506; SHA-256: f0685348c846fac604d0f83eac02cfde2ddaf01e3d6d948bf62f6838987309f8

Table customer_data_primary: 28 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_replica_ap_south: 29 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_replica_eu_west: 28 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_regional_replicas_20260424.sql

Bytes: 36010; SHA-256: f9e72dc994c377d3595c84e1e2481b902711589c02b85bbf6b8d9e28fe7191d3

Table customer_data_primary: 29 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_replica_ap_south: 29 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_replica_eu_west: 31 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_regional_replicas_20260519.sql

Bytes: 32168; SHA-256: aef143d9c25fde14f4f9f1c28782c942aea8bd9b06e5c2407c61ef6d12f77524

Table customer_data_primary: 28 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_replica_ap_south: 29 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_replica_eu_west: 28 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_reporting_replica_20260208.sql

Bytes: 19231; SHA-256: 19e257a0bbaac781d6b55786574a21734a4796e7c8970c76a142848b0ce999df

Table customer_data_primary: 24 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_reporting_replica: 25 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_data_reporting_replica_20260305.sql

Bytes: 20275; SHA-256: fa9a9b0656510065e07013ecc4cf147b91c700400cd21c46cbd963ca22435350

Table customer_data_primary: 25 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

Table customer_data_reporting_replica: 26 rows; fields: resource_id, origin_system, collection_name, record_json, updated_at

## dataset/evidence/databases/customer_search_primary_20260910.sql

Bytes: 826; SHA-256: 91f7c2483af4fcfc69123a047e289e1d5e8dab0a5edc9dcccf188137ae6e825d

Table search_documents_primary: 3 rows; fields: resource_id, display_name, email, source_resource_id, indexed_at

## dataset/evidence/documents/account_history_report_20260718.pdf

Bytes: 65704; SHA-256: abe1877efe69fb5617a79c0d22df9113372e1e6804f8986b0fd408563ecca448

Pages: 2; extracted characters: 720

## dataset/evidence/documents/delivery_correction_attachment.pdf

Bytes: 66039; SHA-256: 0c58960759d4821b030b467d6fe531e83e38e7f50b3de3389a735521d0001f18

Pages: 2; extracted characters: 839

## dataset/evidence/documents/legal_retention_register_20260529.pdf

Bytes: 65857; SHA-256: 0919c931c018565e82502050ee1026918c1baf210c8ba23d2386415dd46efb10

Pages: 2; extracted characters: 1004

## dataset/evidence/documents/security_retention_extract.pdf

Bytes: 64847; SHA-256: 8a6428a899dc8d0769048c8e6f6db70c614fe65fd1e0bb87a43c7927c27ecdda

Pages: 1; extracted characters: 616

## dataset/evidence/images/account_admin_console_20260926.png

Bytes: 124989; SHA-256: d5c32ca5b6e1a2b4bbe9f5d41835ef1fd5d4f7061dab9067a4f9f88cea3c1861

Image: 1800 x 1200; RGB

## dataset/evidence/images/analytics_profile_view_20260713.png

Bytes: 129362; SHA-256: 4e4cb259bc2010b622b0c53fe5872258f994fefc23452a83bb27473758693484

Image: 1800 x 1150; RGB

## dataset/evidence/images/backup_restore_console_20260429.png

Bytes: 155587; SHA-256: 2c246aa5843bec609b9ddfdf1154cd81e0fd61996f83954735e9856e48c18bf3

Image: 1800 x 1150; RGB

## dataset/evidence/images/connector_management_console_20260807.png

Bytes: 130271; SHA-256: e81fabc93ea1b5f4c918d934cdb2bea05d61737adfcc29f281494f5d8ec46355

Image: 1800 x 1150; RGB

## dataset/evidence/images/customer_export_console_20260618.png

Bytes: 134597; SHA-256: 18b95c1bd8b8956e40216df935498a9f3c181ea2a69b5cd6d3c0841a816d5557

Image: 1800 x 1100; RGB

## dataset/evidence/images/deleted_account_reference_20260310.png

Bytes: 136696; SHA-256: 68c28a72afd6ed184d5990d15c543f8a516face204f0360f732755a8a63c28be

Image: 1800 x 1100; RGB

## dataset/evidence/images/marketing_profile_console.png

Bytes: 129711; SHA-256: 51fa0e6a38f8fa3629ba1b0d0b90b4ed139715956b97bfd09a6f1a6232c15df5

Image: 1500 x 920; RGB

## dataset/evidence/images/object_storage_browser_20260213.png

Bytes: 154193; SHA-256: 96e9a191380c29b9e0ab997007268c4cd6353cb6721ebd1ed4a32599d8d37e04

Image: 1800 x 1150; RGB

## dataset/evidence/images/search_index_inspector_20260901.png

Bytes: 121101; SHA-256: 75afdb0ae53a4510c83399a70d88073cb4fb2747454095756e4ddad1a8c70605

Image: 1800 x 1100; RGB

## dataset/evidence/images/security_audit_explorer_20260905.png

Bytes: 147699; SHA-256: ca59f693f4e7002466b3fdeaf1bb6763618770963dd811b60003772d07b4b03b

Image: 1800 x 1100; RGB

## dataset/evidence/images/support_ticket_console_20260524.png

Bytes: 135008; SHA-256: 542b7aec17e6b2f38827896e7eb52c70e4bfaaca22433621be1f80f54884e944

Image: 1800 x 1200; RGB

## dataset/evidence/logs/application_trace_ap_northeast_20260730.log

Bytes: 18839; SHA-256: d624b6045f1f13425969fca642ccfb0762f209764669b17aa3453ad7b212c535

Lines: 93

## dataset/evidence/logs/application_trace_eu_north_20260302.log

Bytes: 24885; SHA-256: 8fbe16d702d95c30f2e74f7d4061c6d2be0e66da6800102b60a4c5542d15e1d9

Lines: 125

## dataset/evidence/logs/cloud_runtime_export_af_south_20260930.log

Bytes: 94518; SHA-256: 00f1ebdfa20c94df4034abcb7d0121b22ab06fc6600ab882aec0ce92b6cc4420

Lines: 305

## dataset/evidence/logs/cloud_runtime_export_us_west_20260608.log

Bytes: 32266; SHA-256: f7740739398d2a1d80e7db3db667b1f93ba93e05b29211df8ef4234c69d1cfd4

Lines: 128

## dataset/evidence/logs/notification_delivery_20260315.log

Bytes: 8972; SHA-256: 3aa3720a9f12f365b3930906d0cfcb991a4476ed7131572a934241e7d555ea4e

Lines: 39

## dataset/evidence/logs/operations_stream_eu_central_20260705.log

Bytes: 26198; SHA-256: 2c2e976c82dac8cdf69ebf89893ebf7a327943a7bcff50383598bcdf05b408ea

Lines: 128

## dataset/evidence/logs/operations_stream_me_central_20260203.log

Bytes: 21199; SHA-256: 0b67c2aeff7f14cdc23e2d878b7ad60ae4651ce7d86b50dca0dc799da9ebf47c

Lines: 103

## dataset/evidence/logs/resource_lookup_trace_20260218_083911.log

Bytes: 10995; SHA-256: 80053c4a6805340cd07179999466518681e547eb8772ca187210068540d7f1e6

Lines: 54

## dataset/evidence/logs/resource_lookup_trace_20260310_061801.log

Bytes: 544; SHA-256: b5dc2e108d33400307aa98e27eca489358e3c5e99296149fe802f8a8d65c141b

Lines: 4

## dataset/evidence/logs/resource_lookup_trace_20260414_054007.log

Bytes: 9836; SHA-256: 08bae0cc919e6a8f0712fe356d84ad5131a2ce24a9de7f07ef16dea1a215d5ac

Lines: 50

## dataset/evidence/logs/resource_lookup_trace_20260509_104353.log

Bytes: 13602; SHA-256: 7a4292a6f8bc08e47d5171a9fb81239f932b1d3bfbfc02bea93be1a17f0de562

Lines: 68

## dataset/evidence/logs/resource_lookup_trace_20260529_074313.log

Bytes: 9626; SHA-256: 05c9facfb1dd25b20a7817145a1721314c9c241bee035ac93b9135ce78dc92a6

Lines: 48

## dataset/evidence/logs/resource_lookup_trace_20260623_053726.log

Bytes: 12014; SHA-256: 42888d566a020c17baede95b419f695c076ea36220facf97a333c54276f2b513

Lines: 60

## dataset/evidence/logs/resource_lookup_trace_20260713_093359.log

Bytes: 10662; SHA-256: b4bb51d58430cb0c1749f67f38417188d558c879d5db0374b05d70fdc059e69d

Lines: 54

## dataset/evidence/logs/resource_lookup_trace_20260728_054417.log

Bytes: 9052; SHA-256: a167b0306dfd1b6364b368395cb9d47bee1a6640d076cf739abc437978be7958

Lines: 46

## dataset/evidence/logs/resource_lookup_trace_20260822_103910.log

Bytes: 9059; SHA-256: 80e7c537ecc51f879b5451e5c28c4f2f82f0aecb0de04b1f4de0eaeddc0b607a

Lines: 46

## dataset/evidence/logs/resource_lookup_trace_20260911_074253.log

Bytes: 12248; SHA-256: b6162ab46f37a376acfef3d889ee0ede18db5e06640569072cd112d16a5ab0b6

Lines: 62

## dataset/evidence/logs/resource_lookup_trace_20260926_103856.log

Bytes: 11743; SHA-256: c9dd4994eca09a613caa2b72527e2fbe454a427e0c1e99bc6ed6c20dd3ce1a80

Lines: 58

## dataset/evidence/logs/search_index_diagnostic_20260906.log

Bytes: 8013; SHA-256: 661b8d05a61f61b9a15b9cf01df0b22e41a4b7dc946a6e800f795e0d5e69bb2c

Lines: 36

## dataset/evidence/logs/service_events_ap_south_20260915.log

Bytes: 22133; SHA-256: 22f51209cfd8b78bd1aecf0ff3219b703dcbc2742cd1150c08a35d8abf170d72

Lines: 104

## dataset/evidence/logs/service_events_sa_east_20260516.log

Bytes: 23481; SHA-256: ecb44c9a642645ae9d0ede7f15ac7ca708ce4a26092b6fbaa4137e56d906f1d3

Lines: 110

## dataset/evidence/logs/structured_service_events_ca_central_20260419.log

Bytes: 38660; SHA-256: f7fe02457df923a082063a15c7202a049466794c5a9f6420a4bafcbdf592f2ff

Lines: 136

## dataset/evidence/logs/structured_service_events_eu_west_20260918.log

Bytes: 31199; SHA-256: 11dcd0aa422607d4d2b90193c9bbf134893b13c889468994304b56e3f76e93a2

Lines: 112

## dataset/evidence/logs/support_replica.log

Bytes: 1863; SHA-256: 4ac921e6044ca6c24f80396a75266a8a41c53a0a32cfdbf40e59229a312a39ce

Lines: 10

## dataset/evidence/logs/syslog_archive_ap_southeast_20260325.log

Bytes: 25968; SHA-256: 3717edbb20eac7ac2ffe6f546d798874fe7416b7f4ae707b47852e604f459258

Lines: 114

## dataset/evidence/logs/syslog_archive_us_east_20260824.log

Bytes: 26414; SHA-256: f8c118b4b1982c4a9c141af380e7158a608d119038c44f1361e5753733a87568

Lines: 118

## dataset/evidence/records/connector_configurations_20260812.json

Bytes: 9788; SHA-256: 6eca1bf09fc230a211605c8bc944652f48fe2ca01aaa3f689f99db1d9d60291d

Top-level: exported_at, origin, record_count, records

## dataset/evidence/records/customer_account_handover_20261001.txt

Bytes: 4488; SHA-256: 202a645baf8364e06abf15ae9acd803ab3c6a3a041ccfbaa82a0d9f38788577c

Lines: 46

## dataset/evidence/records/customer_analytics_report_20260907.json

Bytes: 1351; SHA-256: 58234d55729d1e5efb5e4ac118052461a45605ce769231bd807cfa3990ac26c5

Top-level: captured_at, source, collection, records

## dataset/evidence/records/customer_data_snapshot_bundle_20260131.json

Bytes: 14811; SHA-256: 97faf85f06b1caa159b0ebb8da4c8b6bc9198a65a6271062c7ac7c4ec673cbda

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260223.json

Bytes: 24174; SHA-256: 365958a383a3f569d9ba90b5dae0adcb8cd1ab4fb51a1cdf2822b9f25e440f96

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260322.json

Bytes: 13241; SHA-256: 5b901acb7121073fd50468bc7145010dc8b2360b0fd1d538e5537eed75bdf5d3

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260416.json

Bytes: 13027; SHA-256: 54346b9882559422950af72c12e3ec7a4beca8f4a6f48149009adef04df800cc

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260511.json

Bytes: 25174; SHA-256: 8698f02432b5a32c609931319bff6f7826d80540b90fa3016f40ba4ae13edc91

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260605.json

Bytes: 13830; SHA-256: 2eb4d85beba42e5b136a9cc43427085e10f054ad905962fa4b4f1117fb2663f6

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260630.json

Bytes: 23629; SHA-256: 74c4bbbe0f78ffc341199bcaba990897f03f24f714a0f3a3d3ed733eda8ff738

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260725.json

Bytes: 15328; SHA-256: e02850e508ef81e220ff25c4d2e07b08264ae65fab9d830daa3ed134bc501fbd

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260819.json

Bytes: 13064; SHA-256: a22d01c4f05707e560f5fe3a5d0ffc0b47c329c809e3007b3501a4276cad276a

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260913.json

Bytes: 12146; SHA-256: ed960451d8c52cdf9bac6984f41299419446940da64f822b8b5148b6dcdba567

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260915.json

Bytes: 1843; SHA-256: d35766c60b44d4151877a300686cb2a1006590a55ca224650e53f934e5fb86f6

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_data_snapshot_bundle_20260917.json

Bytes: 17406; SHA-256: 2047d647b1eda5cbf42950222b00bc8c9f6b666ecdaea4504e1d629e5b1810c9

Top-level: exported_at, source, snapshots

## dataset/evidence/records/customer_export_jobs_20260914.json

Bytes: 817; SHA-256: cbe8c9f4f5f57dfe64375ddb585296070c99d9e4cc1a1f438c0e8c427daf2f2a

Top-level: captured_at, source, collection, records

## dataset/evidence/records/customer_export_manifest_20260409.json

Bytes: 11462; SHA-256: e05045570a9cf54a178a3e02618c5bdb04d3db5ded065f060aefd1a4f68bd45c

Top-level: exported_at, origin, record_count, records

## dataset/evidence/records/security_audit_ledger_20261001.json

Bytes: 4985; SHA-256: deb50fa0beeae0761eafa39d50a1df105237f3ee5b668c0a40f78522750f2821

Top-level: exported_at, origin, record_count, records

## dataset/evidence/records/service_resource_export_20260129_114459.json

Bytes: 10387; SHA-256: 2a0d346be2eb908e5b64b4d621e6c154a087ba80bcfb565cab0ce8f6a6e73979

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260228_103637.json

Bytes: 9383; SHA-256: 321a905ab4398ac12e88f4adb00375e31f1d856b3cb042763bca390810867b00

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260320_072349.json

Bytes: 9000; SHA-256: 4abe0e7816818aa435852148e88bc430680741e73baddab0921b10afe215aa27

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260429_083222.json

Bytes: 9691; SHA-256: 4dd5005f93f5db1cef642f0a79bcded07ba21d553da439c62765239c41ed20f6

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260514_114454.json

Bytes: 8733; SHA-256: 59046d0d3f9e64d4767860a1d96e0b373a4e15044945417af201c5048f02061b

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260603_083457.json

Bytes: 9475; SHA-256: 2b11788fb1320bd87e5235008723e0defbc232bac6cf1528f2503e038e5a8e17

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260628_062556.json

Bytes: 8742; SHA-256: b00cd741bc92c0dec39016583e633c9a34d657a67edccb1864f8c46ffc7b9784

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260718_104335.json

Bytes: 10775; SHA-256: e48889623a522b2b59c129b90726d716eb4eb15803f0856ebb80e7e1a6f7b95f

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260807_074104.json

Bytes: 8346; SHA-256: 975d1bc2069c42cd2d77c3f5925eecebaa5d22a8d9d0882b642253bd08f940c2

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260901_053316.json

Bytes: 9390; SHA-256: 57df6065c76474d0c7050a21050eaa1899daf568ad0003f1c32e38541ca960c7

Top-level: exported_at, region, service_exports, source

## dataset/evidence/records/service_resource_export_20260915_114455.json

Bytes: 11804; SHA-256: c900de8f2988a08bf6433ab797e2a249426704ff42d140dd92406e0fae5c6074

Top-level: exported_at, region, service_exports, source

## dataset/evidence_files.csv

Bytes: 11089; SHA-256: f16ef6424f020fd43c9d3a788261a33d96692cbca50d0239fccb9d3e696ee212

Rows: 94

Fields: file_id, file_path, origin, captured_at

## dataset/output.csv

Bytes: 35; SHA-256: 3aa92f75cab5cd10b0ecfcb6b948619a361cca8860dc72dd5e91dccaf9e04e3f

Rows: 0

Fields: case_id, deletion_status, steps_json

## dataset/sample_deletion_requests.csv

Bytes: 9010; SHA-256: fe08461a78fc04f1aadb076c54010ebe2b35bd599a09df2fd014683cc8914c22

Rows: 32

Fields: case_id, email, requested_at, reported_status, reported_at, audit_at, request_text

Audit range: 2026-09-03T11:30:00Z to 2026-10-01T12:00:00Z

## dataset/sample_output.csv

Bytes: 38648; SHA-256: 11bb0f1ab2956e2a8b1b082225b8ef76e07ec112e61e5108cf5819f269eac239

Rows: 32

Fields: case_id, deletion_status, steps_json

Sample statuses: {'COMPLETE': 10, 'INCOMPLETE': 22}

Sample operations: {'VERIFY_RECORD_ABSENT': 50, 'VERIFY_RECORD_PRESENT': 24, 'VERIFY_RECORD_ANONYMIZED': 12, 'REPORT_REMAINING_RECORD': 21, 'DELETE_RECORD': 21, 'REPORT_RESTORE_RISK': 3, 'BLOCK_RESTORE': 3, 'VERIFY_RESTORE_BLOCKED': 6, 'REPORT_EXPOSED_PII': 11, 'REPORT_ACTIVE_DATA_FLOW': 6, 'DISABLE_DATA_FLOW': 6, 'REDACT_RECORD': 6, 'ANONYMIZE_RECORD': 5, 'VERIFY_RECORD_REDACTED': 10, 'VERIFY_DATA_FLOW_DISABLED': 9}

## dataset/system_activity.csv

Bytes: 657360; SHA-256: abc30a185563435905626bbb45519ffaeeaf0ca7d16edde3949ff7596283c20c

Rows: 4011

Fields: activity_id, event_time, event_type, source_system, target_system, resource_id, reported_result, details

event_type: {'INDEX_RECORD': 400, 'UPDATE_RECORD': 672, 'RETAIN_RECORD': 206, 'SEND_EMAIL': 368, 'SYNC_RECORD': 447, 'DELETE_RECORD': 890, 'ANONYMIZE_RECORD': 204, 'REFRESH_CACHE': 284, 'CREATE_EXPORT': 155, 'CHECK_DATA_FLOW': 89, 'CHECK_RESTORE_ACCESS': 28, 'REDACT_RECORD': 173, 'DISABLE_DATA_FLOW': 36, 'BLOCK_RESTORE': 36, 'RESTORE_BACKUP': 1, 'CLASSIFY_REQUEST': 10, 'LINK_RESOURCE_IDENTITY': 12}

reported_result: {'SUCCESS': 2914, 'FAILED': 721, 'PARTIAL': 376}

## dataset/user_audit_log.csv

Bytes: 36709; SHA-256: de04cb620328bad1212f5b1cb0aa05689b5986d5c7cef38ea84e9aebb7b3ca0f

Rows: 306

Fields: audit_id, user_id, event_time, field_name, old_value, new_value

## dataset/user_identities.csv

Bytes: 126411; SHA-256: 63940e0fdc74a85e44463de3a6f18e3b27ff144f08e9981c732dfcfdadece9e6

Rows: 850

Fields: user_id, name, email, phone, email_hash, updated_at

## problem_statement.md

Bytes: 9036; SHA-256: dd478250158b4fe387159ea924493e2dda0404edbbb585c92d9f9bb25237156b

Lines: 162

# All observed JSON structures

- 2: $.records[].metrics: orders_completed_90d, products_viewed_30d, revenue_90d_usd, sessions_30d
- 1: $.records[].recent_activity[]: event, product
- 2: $.records[].recent_activity[]: event, product, quantity
- 2: $.records[]: created_at, download_available, expires_at, file_name, included_sections, owner_email, resource_id
- 2: $.records[]: email, email_hash, metrics, phone, recent_activity, reporting_window, resource_id, user_id
- 105: $.records[]: record_type, recorded_at, resource_id, result, subject_reference, system
- 10: $.service_exports.account_service.profile_lookups[].profile: customer_reference, email, email_hash, full_name, phone
- 47: $.service_exports.account_service.profile_lookups[]: observed_at, profile, resource_id, status_code
- 11: $.service_exports.account_service: profile_lookups
- 48: $.service_exports.analytics_platform.profiles[]: audience_cohort, customer_reference, email, email_hash, observed_at, phone, resource_id
- 11: $.service_exports.analytics_platform: profiles
- 17: $.service_exports.backup_service.restore_entries[]: archive_key, customer_email, customer_reference, observed_at, resource_id, restore_allowed
- 10: $.service_exports.backup_service: restore_entries
- 9: $.service_exports.export_service.exports[]: customer_reference, object_key, observed_at, owner_email, owner_phone, resource_id
- 9: $.service_exports.export_service: exports
- 35: $.service_exports.integration_service.connectors[]: connector_name, customer_email, customer_reference, enabled, last_delivery_status, observed_at, resource_id
- 11: $.service_exports.integration_service: connectors
- 58: $.service_exports.search_service.index_queries[].hits.documents[]: customer_reference, display_name, email, email_hash, phone, resource_id
- 58: $.service_exports.search_service.index_queries[].hits: documents, total
- 58: $.service_exports.search_service.index_queries[]: hits, observed_at, query, resource_id
- 11: $.service_exports.search_service: index_queries
- 37: $.service_exports.security_service.audit_records[]: event_code, observed_at, resource_id, retention_until, subject_reference
- 11: $.service_exports.security_service: audit_records
- 45: $.service_exports.support_platform.tickets[]: customer_reference, message_excerpt, observed_at, requester_email, requester_name, requester_phone, resource_id
- 11: $.service_exports.support_platform: tickets
- 8: $.service_exports: account_service, analytics_platform, backup_service, export_service, integration_service, search_service, security_service, support_platform
- 2: $.service_exports: account_service, analytics_platform, backup_service, integration_service, search_service, security_service, support_platform
- 1: $.service_exports: account_service, analytics_platform, export_service, integration_service, search_service, security_service, support_platform
- 61: $.snapshots[].records[].document: customer_reference, display_name, email
- 50: $.snapshots[].records[].metrics: orders_completed_90d, products_viewed_30d, revenue_90d_usd, sessions_30d
- 83: $.snapshots[].records[].recent_activity[]: event, product
- 43: $.snapshots[].records[].recent_activity[]: event, product, quantity
- 25: $.snapshots[].records[]: account_status, customer_reference, email, full_name, phone, resource_id, signup_channel
- 2: $.snapshots[].records[]: account_status, email, email_hash, name, phone, resource_id, subject_reference
- 112: $.snapshots[].records[]: actor_type, event_name, integrity_seal, resource_id, subject_reference
- 18: $.snapshots[].records[]: archive_path, encryption, resource_id, restore_allowed, subject_reference
- 41: $.snapshots[].records[]: channel, message_text, resource_id, subject_reference, ticket_id
- 37: $.snapshots[].records[]: connector_name, destination, enabled, mode, resource_id, subject_selector
- 6: $.snapshots[].records[]: created_at, download_available, expires_at, file_name, included_sections, owner_email, resource_id
- 61: $.snapshots[].records[]: document, index_name, resource_id
- 50: $.snapshots[].records[]: email, email_hash, metrics, phone, recent_activity, reporting_window, resource_id, user_id
- 7: $.snapshots[].records[]: file_name, resource_id, storage_class, ticket_id, uploaded_by
- 124: $.snapshots[].records[]: lookup_value, record_type, recorded_at, resource_id, result, system
- 2: $.snapshots[].records[]: order_reference, resource_id, retained_until, retention_reason, subject_reference
- 116: $.snapshots[]: captured_at, collection, data_store, records
- 2: $: captured_at, collection, records, source
- 3: $: exported_at, origin, record_count, records
- 11: $: exported_at, region, service_exports, source
- 12: $: exported_at, snapshots, source
