CREATE TABLE IF NOT EXISTS projects (
                                        project_id SERIAL PRIMARY KEY,
                                        name VARCHAR(255) UNIQUE NOT NULL,
                                        is_new_building BOOLEAN,
                                        climate VARCHAR(50),
                                        location VARCHAR(255),
                                        cte_version VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS spaces (
                                      id UUID PRIMARY KEY,
                                      project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
                                      name VARCHAR(255),
                                      stype VARCHAR(50),
                                      polygon TEXT,
                                      height REAL,
                                      x REAL,
                                      y REAL,
                                      z REAL,
                                      angle_with_building_north REAL,
                                      insidete INTEGER,
                                      floor TEXT,
                                      power REAL,
                                      veei_obj REAL,
                                      veei_ref REAL,
                                      spacetype TEXT,
                                      spaceconds TEXT,
                                      systemconds TEXT,
                                      floor_multiplier REAL,
                                      multiplier REAL,
                                      ismultiplied INTEGER,
                                      airchanges_h REAL,
                                      UNIQUE (project_id, name)
);

CREATE TABLE IF NOT EXISTS walls (
                                     id UUID PRIMARY KEY,
                                     project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
                                     space_id UUID REFERENCES spaces(id),
                                     name VARCHAR(255),
                                     cons TEXT,
                                     location TEXT,
                                     x REAL,
                                     y REAL,
                                     z REAL,
                                     angle_with_space_north REAL,
                                     tilt REAL,
                                     polygon TEXT,
                                     bounds TEXT,
                                     nextto TEXT,
                                     UNIQUE (project_id, name)
);

CREATE TABLE IF NOT EXISTS windows (
                                       id UUID PRIMARY KEY,
                                       project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
                                       wall_id UUID REFERENCES walls(id),
                                       name VARCHAR(255),
                                       cons TEXT,
                                       x REAL,
                                       y REAL,
                                       height REAL,
                                       width REAL,
                                       setback REAL,
                                       coefs TEXT,
                                       overhang_a REAL,
                                       overhang_b REAL,
                                       overhang_depth REAL,
                                       overhang_width REAL,
                                       overhang_angle REAL,
                                       left_fin_a REAL,
                                       left_fin_b REAL,
                                       left_fin_depth REAL,
                                       left_fin_height REAL,
                                       right_fin_a REAL,
                                       right_fin_b REAL,
                                       right_fin_depth REAL,
                                       right_fin_height REAL,
                                       louvres_is_horizontal INTEGER,
                                       louvres_width REAL,
                                       louvres_distance REAL,
                                       louvres_angle REAL,
                                       louvres_transmisivity REAL,
                                       louvres_reflectivity REAL,
                                       UNIQUE (project_id, name)
);

CREATE TABLE IF NOT EXISTS wallcons (
                                        id UUID PRIMARY KEY,
                                        project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
                                        name TEXT,
                                        group_name TEXT,
                                        absorptance REAL,
                                        UNIQUE (project_id, name)
);

CREATE TABLE IF NOT EXISTS wallcons_layers (
                                               id UUID PRIMARY KEY,
                                               wallcons_id UUID REFERENCES wallcons(id) ON DELETE CASCADE,
                                               layer_order INTEGER,
                                               material TEXT,
                                               thickness REAL,
                                               UNIQUE(wallcons_id, layer_order)
);

CREATE TABLE IF NOT EXISTS wincons (
                                       id UUID PRIMARY KEY,
                                       project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
                                       name TEXT,
                                       group_name TEXT,
                                       glass TEXT,
                                       glassgroup TEXT,
                                       frame TEXT,
                                       framegroup TEXT,
                                       framefrac REAL,
                                       infcoeff REAL,
                                       deltau REAL,
                                       gglshwi REAL,
                                       UNIQUE (project_id, name)
);

CREATE TABLE IF NOT EXISTS materials (
                                         id UUID PRIMARY KEY,
                                         project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
                                         name TEXT,
                                         material_group TEXT,
                                         thickness REAL,
                                         conductivity REAL,
                                         density REAL,
                                         specificheat REAL,
                                         vapourdiffusivity REAL,
                                         resistance REAL,
                                         UNIQUE (project_id, name)
);

CREATE TABLE IF NOT EXISTS thermal_bridges (
                                               id UUID PRIMARY KEY,
                                               project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
                                               name TEXT,
                                               bridge_type TEXT,
                                               length REAL,
                                               psi_value REAL,
                                               frsi REAL,
                                               partition TEXT,
                                               anglemin REAL,
                                               anglemax REAL,
                                               catalog_classes TEXT,
                                               catalog_pcts TEXT,
                                               catalog_firstelems TEXT,
                                               catalog_secondelems TEXT,
                                               UNIQUE (project_id, name)
);

select  wc.project_id, wc.name, wc.group_name, wc.absorptance
from wallcons wc,projects pr
where wc.project_id=pr.project_id and pr.name='Ejemplo1_2526_Config1';


select wcl.* from wallcons_layers wcl, wallcons wc, projects pr
where wcl.wallcons_id=wc.id and wc.project_id=pr.project_id and pr.name='Ejemplo1_2526_Config1';

select m.* from materials m, projects pr where m.project_id=pr.project_id and pr.name='Ejemplo1_2526_Config1';

select win.* from windows win, walls w, spaces s, projects pr
where win.wall_id=w.id and w.space_id=s.id and s.project_id=pr.project_id and pr.name='Ejemplo1_2526_Config1';

select wc.* from wincons wc, projects pr where wc.project_id=pr.project_id and pr.name='Ejemplo1_2526_Config1';
