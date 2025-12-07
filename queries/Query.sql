create table grupo
(
    NAME  text
        constraint PK_temp_grupo
            primary key,
    IMAGE text,
    TYPE  text,
    constraint CH_temp_grupo_type
        check (TYPE IN ('C', 'U'))
);

create table material
(
    NAME          text
        constraint PK_temp_material
            primary key,
    THICKNESS     REAL,
    CONDUCTIVITY  REAL,
    DENSITY       REAL,
    SPECIFIC_HEAT REAL,
    VAPOUR_DF     REAL,
    IMAGE         text,
    TYPE          text,
    GRUPO         text
        constraint FK_temp_material
            references grupo,
    constraint CH_temp_material_type
        check (TYPE IN ('C', 'U'))
);

