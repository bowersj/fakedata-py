copy fakedata.geoname (geonameid,name,asciiname,alternatenames,latitude,longitude,fclass,fcode,country,cc2,admin1,admin2,admin3,admin4,population,elevation,gtopo30,timezone,moddate) from '/opt/data/allCountries.txt' null as '';
copy fakedata.alternatename  (alternatenameid,geonameid,isolanguage,alternatename,ispreferredname,isshortname,iscolloquial,ishistoric) from '/opt/data/alternateNames.txt' null as '';
copy fakedata.countryinfo (iso_alpha2,iso_alpha3,iso_numeric,fips_code,name,capital,areainsqkm,population,continent,tld,currencycode,currencyname,phone,postalcode,postalcoderegex,languages,geonameid,neighbors,equivfipscode) from '/opt/data/countryInfo.txt' null as '';
copy fakedata.iso_languagecodes (iso_639_3,iso_639_2,iso_639_1,language_name) from '/opt/data/iso-languagecodes.txt' null as '';
copy fakedata.admin2CodesAscii (code,name,nameAscii,geonameid) from '/opt/data/admin2Codes.txt' null as '';
copy fakedata.featureCodes (code,name,description) from '/opt/data/featureCodes_en.txt' null as '';
copy fakedata.timeZones (countryCode,timeZoneId,GMT_offset,DST_offset,raw_offset) from '/opt/data/timeZones.txt' null as '';
copy fakedata.postalcodes (countrycode,postalcode,placename,admin1name,admin1code,admin2name,admin2code,admin3name,admin3code,latitude,longitude,accuracy) from '/opt/data/allPostalCodes.txt' null as '';