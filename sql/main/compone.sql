create table compone
(
    NAME_CERR text
        constraint PK_compone_cerr
            references cerramiento,
    NAME_MAT  text
        constraint PK_compone_mat
            references material,
    ORDEN     NUMBER(5),
    THICKNESS NUMBER(5, 5),
    constraint PK_compone
        primary key (NAME_CERR, NAME_MAT, ORDEN)
);

