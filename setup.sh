#! /bin/sh
# script to setup the postgis database and setup the respective database tables


#create a postgis spatial database template

POSTGIS_SQL_PATH=/usr/local/Cellar/postgis/2.0.3/share/postgis/
#POSTGIS_SQL_PATH=/usr/share/postgresql/8.4/contrib
dropdb   template_postgis1
createdb  -E UTF8 template_postgis1 # Create the template spatial database.
createlang  -d template_postgis1 plpgsql # Adding PLPGSQL language support.
psql  -d postgres -c "UPDATE pg_database SET datistemplate='true' WHERE datname='template_postgis1';"
#psql  -d template_postgis1 -f $POSTGIS_SQL_PATH/postgis.sql # Loading the PostGIS SQL routines
psql  -d template_postgis1 -f $POSTGIS_SQL_PATH/postgis.sql # Loading the PostGIS SQL routines
psql  -d template_postgis1 -f $POSTGIS_SQL_PATH/spatial_ref_sys.sql
psql  -d template_postgis1 -c "GRANT ALL ON geometry_columns TO PUBLIC;" # Enabling users to alter spatial tables.
psql   -d template_postgis1 -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"

# create the database (first drop the old one, if it exists)
#
dropdb   geoserver
createdb   geoserver -T template_postgis1

#create a table to contain district name, slug,and poll info (yes,or no)
#sudo -u postgres psql -d geoserver  -c "create table district (id char(5), district varchar(100), slug varchar(100),iso_code varchar(5), poll_id integer ,poll_result varchar(3));"

# load the shapefile
#
ogr2ogr -f  "PGDump" -t_srs EPSG:900913 geoserver.sql Uganda_District2010/Uganda_districts2010.shp  -nlt multipolygon -nln Uganda_districts2010

