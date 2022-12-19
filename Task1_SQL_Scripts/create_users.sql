-- Read-write
CREATE ROLE read_write;

GRANT CONNECT ON DATABASE cdm TO read_write;
GRANT USAGE, CREATE ON SCHEMA cdm_schema TO read_write;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA cdm_schema TO read_write;
ALTER DEFAULT PRIVILEGES IN SCHEMA cdm_schema GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO read_write;

GRANT USAGE ON ALL SEQUENCES IN SCHEMA cdm_schema TO read_write;
ALTER DEFAULT PRIVILEGES IN SCHEMA cdm_schema GRANT USAGE ON SEQUENCES TO read_write;

CREATE USER
    user1
WITH PASSWORD
    'user1_password';

GRANT read_write TO user1;


- Read-only
CREATE ROLE read_only;

GRANT CONNECT ON DATABASE cdm TO read_only;
GRANT USAGE ON SCHEMA cdm_schema TO read_only;

GRANT SELECT ON ALL TABLES IN SCHEMA cdm_schema TO read_only;
ALTER DEFAULT PRIVILEGES IN SCHEMA cdm_schema GRANT SELECT ON TABLES TO read_only;

CREATE USER
    readonly
WITH PASSWORD
    'user1_password';

GRANT read_only TO readonly;