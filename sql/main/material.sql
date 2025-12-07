create table material
(
    NAME          text
        constraint PK_material
            primary key,
    THICKNESS     NUMBER(5, 5),
    CONDUCTIVITY  NUMBER(5, 5),
    DENSITY       NUMBER(5, 5),
    SPECIFIC_HEAT NUMBER(5, 5),
    VAPOUR_DF     NUMBER(5, 5),
    IMAGE         text,
    TYPE          text,
    GRUPO         text
        constraint FK_material
            references grupo,
    constraint CH_material_type
        check (TYPE IN ('C', 'U'))
);

