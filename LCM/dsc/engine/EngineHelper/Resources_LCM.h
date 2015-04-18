/*
**==============================================================================
**
** Open Management Infrastructure (OMI)
**
** Copyright (c) Microsoft Corporation. All rights reserved. See license.txt for license information.
**
** Licensed under the Apache License, Version 2.0 (the "License"); you may not
** use this file except in compliance with the License. You may obtain a copy
** of the License at
**
**     http://www.apache.org/licenses/LICENSE-2.0
**
** THIS CODE IS PROVIDED *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
** KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
** WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
** MERCHANTABLITY OR NON-INFRINGEMENT.
**
** See the Apache 2 License for the specific language governing permissions
** and limitations under the License.
**
**==============================================================================
*/
/*EngineHelper takes ID numbers from 1001 - 1100*/

#ifndef __RESOURCES_LCM_H_
#define __RESOURCES_LCM_H_

#define ID_ENGINEHELPER_MEMORY_ERROR 1001
#define ID_ENGINEHELPER_FILESIZE_ERROR 1002
#define ID_ENGINEHELPER_OPENFILE_ERROR 1003
#define ID_ENGINEHELPER_READFILE_ERROR 1004
#define ID_ENGINEHELPER_GETFILESIZE_ERROR 1005
#define ID_ENGINEHELPER_CAT_ERROR 1006
#define ID_ENGINEHELPER_CREATEPROCESS_ERROR 1007
#define ID_ENGINEHELPER_REGISTERCIMPROV_ERROR 1008
#define ID_ENGINEHELPER_CHECKSUMGEN_ERROR 1009
#define ID_ENGINEHELPER_FAILEDTO_DESIREDSTATE 1010
#define ID_ENGINEHELPER_PSINFRA_LOADERROR 1011
#define ID_ENGINEHELPER_MANUAL_FAILED 1012
#define ID_ENGINEHELPER_GET_PROPERTY_X_FROM_Y_FAILED 1014

/*LCMHelper takes ID numbers from 1101 - 1200*/

#define ID_LCMHELPER_ETWREGISTREATION_FAILED 1101
#define ID_LCMHELPER_INIT_AGENTCRITSEC_FAILED 1102
#define ID_LCMHELPER_INIT_FILECRITSEC_FAILED 1103
#define ID_LCMHELPER_INIT_EXAPANDENV_FAILED 1104
#define ID_LCMHELPER_ETWUNREGISTREATION_FAILED 1105
#define ID_LCMHELPER_VALIDATE_CONFGDIR_FAILED 1106
#define ID_LCMHELPER_DEL_GETFILEBEFORE_FAILED 1107
#define ID_LCMHELPER_SAVE_GETCONF_FAILED 1108
#define ID_LCMHELPER_LOAD_GETFILE_FAILED 1109
#define ID_LCMHELPER_GET_CONF_FAILED 1110
#define ID_LCMHELPER_DEL_GETFILEAFTER_FAILED 1111
#define ID_LCMHELPER_CREATE_CONFDIR_FAILED 1112
#define ID_LCMHELPER_MEMORY_ERROR 1113
#define ID_LCMHELPER_PRINTF_ERROR 1114
#define ID_LCMHELPER_OLDCONFPENDING_ERROR 1115
#define ID_LCMHELPER_SAVE_PENDING_ERROR 1116
#define ID_LCMHELPER_LOAD_PENDING_ERROR 1117
#define ID_LCMHELPER_SENDCONFIGAPPLY_ERROR 1118
#define ID_LCMHELPER_DEL_PENDINGFILEAFTER_FAILED 1119
#define ID_LCMHELPER_COPY_FAILED 1120
#define ID_LCMHELPER_CONVERT_SECDESC_FAILED 1121
#define ID_LCMHELPER_CREATE_CONF_FAILED 1122
#define ID_LCMHELPER_META_MOF_FAILED 1123
#define ID_LCMHELPER_MODLOADNULL_FAILED 1124
#define ID_LCMHELPER_METASCHEMA_LOADNULL_FAILED 1125
#define ID_LCMHELPER_METASCHEMA_NAMEMISMATCH_FAILED 1126
#define ID_LCMHELPER_METASCHEMA_CREATESERIALIZE_FAILED 1127
#define ID_LCMHELPER_METASCHEMA_SERIALIZE_FAILED 1128
#define ID_LCMHELPER_METASCHEMA_DELETE_FAILED 1129
#define ID_LCMHELPER_DESERIALIZER_CREATE_FAILED 1130
#define ID_LCMHELPER_METASCHEMA_CLONE_FAILED 1131
#define ID_LCMHELPER_TASK_CREATEPARAM_FAILED 1132
#define ID_LCMHELPER_TASK_ADDPARAM_FAILED 1133
#define ID_LCMHELPER_TASK_CREATESESSION_FAILED 1134
#define ID_LCMHELPER_EXPANDENV_FAILED 1135
#define ID_LCMHELPER_THREADIMPERSONATION_FAILED 1136
#define ID_LCMHELPER_REVERTSELF_FAILED 1137
#define ID_LCMHELPER_RESUMEIMPERSONATION_FAILED 1138
#define ID_LCMHELPER_CONSTRUCTGET_FAILED 1139
#define ID_LCMHELPER_WRITEGET_FAILED 1140
#define ID_LCMHELPER_SETGET_FAILED 1141
#define ID_LCMHELPER_POSTGET_FAILED 1142
#define ID_LCMHELPER_CONSTRUCTAPPLY_FAILED 1143
#define ID_LCMHELPER_SETAPPLY_FAILED 1144
#define ID_LCMHELPER_POSTAPPLY_FAILED 1145
#define ID_LCM_WRITEMESSAGE_REBOOT 1150
#define ID_LCM_WRITEMESSAGE_STARTCONSISTENCY 1151
#define ID_LCM_WRITEMESSAGE_ENDCONSISTENCY 1152
#define ID_LCM_WRITEMESSAGE_CONSISTENCY_PENDINGEXIST 1153
#define ID_LCM_WRITEMESSAGE_CONSISTENCY_CURRENTEXIST 1154
#define ID_LCM_WRITEMESSAGE_SAVETOPENDING 1155
#define ID_LCMHELPER_NORESOURCESPECIFIED 1156
#define ID_LCMHELPER_COMPUTERNAMECONTEXT_ERROR 1157
#define ID_LCMHELPER_GETTOKENINFOSIZE_ERROR 1158
#define ID_LCM_REPUDIATIONMSG 1159
#define ID_LCMHELPER_SAVE_METATMP_ERROR 1160
#define ID_LCMHELPER_DEL_METATMPFILEAFTER_FAILED 1161
#define ID_LCMHELPER_DEL_FAILED 1162
#define ID_LCM_PULL_GETACTION_NORESULTSTATUS 1163
#define ID_LCM_PULL_GETACTION_UNEXPECTEDRESULTSTATUS 1164
#define ID_LCM_PULL_GETCONF_UNEXPECTEDRESULTSTATUS 1165
#define ID_LCM_PULL_GETCONF_NORESULTSTATUS 1166
#define ID_LCM_CONF_DATAEXIST 1167
#define ID_LCMHELPER_CONSTRUCTTEST_FAILED 1168
#define ID_LCMHELPER_SETTEST_FAILED 1169
#define ID_LCMHELPER_POSTTEST_FAILED 1170
#define ID_LCMHELPER_CURRENT_NOTFOUND 1171
#define ID_LCM_WRITEMESSAGE_ENDTESTPROCESSING_FAIL 1173
#define ID_LCM_TIMEMESSAGE 1174
#define ID_LCM_FORCE_PARAMETER_INVALIDVALUE 1175
#define ID_LCM_FAILED_TO_GET_METACONFIGURATION 1176
#define ID_CONSISTENCY_TASK_FAILURE 1177
#define ID_PULLSERVER_TASK_FAILURE 1178
#define ID_LCMHELPER_SHUTDOWN_FAILED 1179
#define ID_LCMHELPER_SHUTDOWN_MESSAGE 1180
#define ID_LCM_PUSH_REQUESTED_ON_PULL_WO_FORCE 1181
#define ID_LCMHELPER_PREVIOUS_NOTFOUND 1182
#define ID_LCM_CONF_NUMBEREXIST 1183
#define ID_LCM_MULTIPLE_METHOD_REQUEST 1186
#define ID_LCMHELPER_UNEXPECTED_TASKNAME_ERROR 1187
#define ID_LCMHELPER_INVALID_INTERVAL_ERROR 1188
#define ID_LCMHELPER_DELETEFILE_ERROR 1189
#define ID_LCMHELPER_GETTEMPPATH_ERROR 1190
#define ID_LCMHELPER_GETTEMPFILENAME_ERROR 1191
#define ID_LCMHELPER_CREATEFILE_ERROR 1192
#define ID_LCMHELPER_WRITEFILE_ERROR 1193
#define ID_LCMHELPER_CLOSEHANDLE_ERROR 1194
#define ID_LCMHELPER_STRLEN_ERROR 1195
#define ID_LCM_WRITEMESSAGE_ENDTESTPROCESSING_TRUE 1196
#define ID_LCM_WRITEMESSAGE_ENDTESTPROCESSING_FALSE 1197
#define ID_LCM_CLEAR_PROVIDER_CACHE 1198
#define ID_LCM_CLEAR_PROVIDER_CACHE_FAILED 1199
#define ID_LCM_CREATE_PULL_RUN_LOG_FILE 1200

/*Module Manager takes ID numbers from 1201 - 1300*/

#define ID_MODMAN_MODMAN_NULLPARAM 1201
#define ID_MODMAN_APPINIT_FAILED 1202
#define ID_MODMAN_PARAM_INVALID 1203
#define ID_MODMAN_LOADDOC_NULLPARAM 1204
#define ID_MODMAN_GETREG_NULLPARAM 1205
#define ID_MODMAN_REGINS_NOTFOUND 1206
#define ID_MODMAN_CONFIGCLASS_NOTREG 1207
#define ID_MODMAN_GETCOMPAT_NULLPARAM 1208
#define ID_MODMAN_GETFILTERED_FAILED 1209
#define ID_MODMAN_NEWOO_FAILED 1210
#define ID_MODMAN_OOSET_FAILED 1211
#define ID_MODMAN_FINDFIRST_FAILED 1212
#define ID_MODMAN_FINDNEXT_FAILED 1213
#define ID_MODMAN_SYSTEMCACHE_INVALIDPARAM 1214
#define ID_MODMAN_SCHEMAFROMMOF_INVALIDPARAM 1215
#define ID_MODMAN_FILTER_RESOURCEID 1216
#define ID_MODMAN_FILTER_MULTIPLEINS 1217
#define ID_MODMAN_FILTER_NOINSTANCE 1218
#define ID_MODMAN_MAPPING_CLASSNAME_NOTFOUND 1219
#define ID_MODMAN_FILTER_ARGNULL 1220
#define ID_MODMAN_GETELEMENT_FAILED 1221
#define ID_MODMAN_VALIDATE_INFRASCHEMA 1222
#define ID_MODMAN_VALIDATE_PROVREG_MULTI 1223
#define ID_MODMAN_VALIDATE_PROVREG_MANDATORY 1224
#define ID_MODMAN_VALIDATE_PROVREG_NOCLASS 1225
#define ID_MODMAN_VALIDATE_PROVREG_NOREG 1226
#define ID_MODMAN_VALIDATE_SCHEMA_INVPARAM 1227
#define ID_MODMAN_VALIDATE_SCHEMA_NOMETHOD 1228
#define ID_MODMAN_VALIDATE_SCHEMA_VERSIONQUAL 1229
#define ID_MODMAN_VALIDATE_SCHEMA_NOSUPP_REF 1230
#define ID_MODMAN_VALIDATE_SCHEMA_NOMANDATORY_QUALIFIER 1231
#define ID_MODMAN_VALIDATE_SCHEMA_NOKEY 1232
#define ID_MODMAN_VALIDATE_PROVSCHEMA_NORES 1233
#define ID_MODMAN_VALIDATE_PROVSCHEMA_NOTREFERRED 1234
#define ID_MODMAN_VALIDATE_PROVSCHEMA_ONERES 1235
#define ID_MODMAN_VALIDATE_PROVSCHEMA_NOMANDATORY 1236
#define ID_MODMAN_VALIDATE_PROVREGINS_CLASSNAME 1237
#define ID_MODMAN_VALIDATE_PROVREGINS_TYPE 1238
#define ID_MODMAN_VALIDATE_PROVREGINS_PROP_CLASSNAME 1239
#define ID_MODMAN_VALIDATE_PROVREGINS_PROP_COMPATVERSION 1240
#define ID_MODMAN_VALIDATE_PROVREGINS_PROP_MODULEVERSION 1241
#define ID_MODMAN_VALIDATE_PROVREGINS_PROP_NAMESPACE 1242
#define ID_MODMAN_VALIDATE_PROVREGINS_PROP_MODULENAME 1243
#define ID_MODMAN_VALIDATE_CLASSPROP_MAND_NAME 1244
#define ID_MODMAN_VALIDATE_CLASSPROP_MAND_TYPE 1245
#define ID_MODMAN_VALIDATE_CLASSPROP_MAND_GETCLASS 1246
#define ID_MODMAN_VALIDATE_CLASSPROP_MAND_NOMATCH 1247
#define ID_MODMAN_VALIDATE_BASERES_NOQUAL 1248
#define ID_MODMAN_VALIDATE_BASERES_PSDERIVATEION 1249
#define ID_MODMAN_VALIDATE_MAPPING_NAMESPACE 1250
#define ID_MODMAN_VALIDATE_MAPPING_PARAM_GET 1251
#define ID_MODMAN_VALIDATE_MAPPING_PARAM_TEST 1252
#define ID_MODMAN_VALIDATE_MAPPING_PARAM_SET 1253
#define ID_MODMAN_VALIDATE_MAPPING_PARAM_ALLFAILED 1254
#define ID_MODMAN_VALIDATE_BASERES_V2DERIVATEION 1255
#define ID_MODMAN_WINDIRENV_FAILED 1256
#define ID_MODMAN_VALIDATE_DOCINS_VERSION 1257
#define ID_MODMAN_DUPLICATE_RESOURCEID 1258
#define ID_MODMAN_METACONFIG_MERGED_WITH_OTHERCONFIG 1259
#define ID_MODMAN_METACONFIG_NOTFOUND_OR_MORE 1260
#define ID_LCM_WRITEMESSAGE_STARTPROCESSREBOOT 1261
#define ID_LCM_WRITEMESSAGE_REBOOT_PENDINGEXIST 1262
#define ID_LCM_WRITEMESSAGE_REBOOT_CURRENTEXIST 1263
#define ID_LCM_WRITEMESSAGE_ENDPROCESSREBOOT 1264
#define ID_MODMAN_VALIDATE_VERSIONCOMPATIBILITYMETACONFIG 1265
#define ID_MODMAN_VALIDATE_DOCINS 1266
#define ID_MODMAN_VALIDATE_VERSIONNUMBER 1267
#define ID_MODMAN_VALIDATE_SIZEOF_ARRAYCONFIGDOWNLOADMANAGER 1268
#define ID_LCM_VALIDATE_DOWNLOADMANAGERNAMES 1269
#define ID_LCM_VALIDATE_ALLOWUNSECURECONNECTION 1270

/*CAInfrastructure takes ID numbers from 1301 - 1400*/


#define ID_CAINFRA_DEPENDCY_NULLPARAM 1301
#define ID_CAINFRA_DEPENDCY_CYCLE 1302
#define ID_CAINFRA_DEPENDCY_OUTOFBOUNDS 1303
#define ID_CAINFRA_INSTANCE_RESOURCEID 1304
#define ID_CAINFRA_INSTANCE_RESOURCEID_NOTFOUND 1305
#define ID_CAINFRA_DEPENDCYRESOLVER_OUTOFBOUNDS 1306
#define ID_CAINFRA_GET_NULLPARAM 1307
#define ID_CAINFRA_NEWSESSION_FAILED 1308
#define ID_CAINFRA_UNKNOWN_REGISTRATION 1309
#define ID_CAINFRA_GET_NAMESPACE_FAILED 1310
#define ID_CAINFRA_GET_NEWAPPLICATIONINSTANCE_FAILED 1311
#define ID_CAINFRA_GET_ADDELEM_FAILED 1312
#define ID_CAINFRA_GETINSTANCE_FAILED 1313
#define ID_CAINFRA_GET_RETURNVALUE_FAILED 1314
#define ID_CAINFRA_GET_RESULT_FAILED 1315
#define ID_CAINFRA_GET_PROVCONTEXT_FAILED 1316
#define ID_CAINFRA_GET_OUTPUTRES_FAILED 1317
#define ID_CAINFRA_CLONE_FAILED 1318
#define ID_CAINFRA_GETEXECUTION_FAILED 1319
#define ID_CAINFRA_GET_LOGRESOURCE_FAILED 1320
#define ID_CAINFRA_TESTEXECUTION_FAILED 1321
#define ID_CAINFRA_DEPENDCY_CYCLE2 1328
#define ID_CAINFRA_INSTANCE_RESOURCEID_NOTFOUND2 1329
#define ID_CA_MOVETODESIREDSTATE_FAILED_APPEND_RESOURCEID 1330
#define ID_CA_SET_TIMEMESSAGE 1332
#define ID_CA_GET_TIMEMESSAGE 1333
#define ID_CA_TEST_TIMEMESSAGE 1334
#define ID_CA_CRYPTO_STORE_UNOPENED 1335
#define ID_CA_CRYPTO_CERT_NOTFOUND 1336
#define ID_CA_CRYPTO_KEY_CONTEXT_FAILED 1337
#define ID_CA_CRYPTO_GET_PUBLIC_KEY_FAILED 1338
#define ID_CA_CRYPTO_GET_PRIVATE_KEY_FAILED 1339
#define ID_CA_CRYPTO_ENCRYPTED_MALLOC_FAILED 1340
#define ID_CA_CRYPTO_ENCRYPTION_FAILED 1341
#define ID_CA_CRYPTO_DECRYPTED_MALLOC_FAILED 1342
#define ID_CA_CRYPTO_DECRYPTION_FAILED 1343
#define ID_CA_CRYPTO_UPDATE_PWD_FAILED 1344
#define ID_CA_FAILED_TO_GET_METACONFIGURATION 1355
#define ID_CA_CANCEL_CONFIGURATION 1356 
#define ID_CA_FAILED_TO_WAIT_EVENT 1357 
#define ID_CA_CANCELWMIV2_FAILED 1358
#define ID_CA_DUPLICATE_KEYS 1359
#define ID_CA_COMMA_SEPARATOR 1360
#define ID_CAINFRA_GET_NEWOPERATIONOPTIONS_FAILED 1361
#define ID_CAINFRA_GET_SETCUSTOMOPTION_FAILED 1362
#define ID_LCM_CONFIRM_NOT_SUPPORTED 1363


// Formatting output 1401 to 1500

#define ID_OUTPUT_FORMATOUTPUT 1401 
#define ID_OUTPUT_FORMATPROVIDER 1402 
#define ID_OUTPUT_OPERATION_START 1403
#define ID_OUTPUT_OPERATION_END 1404
#define ID_OUTPUT_OPERATION_FAILED 1405
#define ID_OUTPUT_ITEM_TEST 1406
#define ID_OUTPUT_ITEM_GET 1407
#define ID_OUTPUT_ITEM_SET 1408
#define ID_OUTPUT_ITEM_RESOURCE 1409
#define ID_OUTPUT_ITEM_ROLLBACK 1410
#define ID_OUTPUT_EMPTYSTRING 1411
#define ID_OUTPUT_OPERATION_SKIP 1412
#define ID_OUTPUT_FORMATNORESOURCE 1413

/*LCMHelper takes ID numbers from 1501 - 1600 (continuing)*/
#define ID_LCM_WRITEMESSAGE_REBOOTMANUALLY 1501
#define ID_LCMHELPER_OVERWROTE_USER_SPECIFIED_REFRESH_FREQUENCY 1502
#define ID_LCMHELPER_OVERWROTE_USER_SPECIFIED_CONFMODE_FREQUENCY 1503
#define ID_LCMHELPER_METAMOFCORRUPTED 1504
#define ID_LCM_PULL_GETLCMUPDATE_NORESULTSTATUS 1505
#define ID_LCM_PUSH_GETDEPENDS_FAILED 1506
#define ID_LCM_FORCEOPERATION_TERMINATED 1507
#define ID_LCMHELPER_DELETE_COMPARE_ERROR 1508
#define ID_LCMHELPER_SAVE_COMPARE_ERROR 1509
#define ID_LCMHELPER_COMPARE_NOTFOUND 1510
#define ID_LCM_WRITEMESSAGE_ENDCOMPAREPROCESSING_TRUE 1511
#define ID_LCM_WRITEMESSAGE_ENDCOMPAREPROCESSING_FALSE 1512
#define ID_LCM_ERROR_RENAME_BUILT_IN_PROVIDER 1513
#define ID_LCM_GETRESOURCESTATE_INVALID_PARAMETER 1514
#define ID_LCMHELPER_SAVE_PARTIALCONFIGDATASTORE_ERROR 1515
#define ID_LCM_CANNOTUSE_PARTIALCONFIG_PUSHMODE_WITHOUTPUBLISH 1516
#define ID_LCMHELPER_PARTIALCONFIGNAME_NOT_SET 1517
#define ID_LCMHELPER_ERRORMERGING_PARTIALCONFIGS 1518
#define ID_LCMHELPER_ERROR_DURING_SERIALIZING 1519
#define ID_LCMHELPER_ERROR_WRITINGFILE 1520
#define ID_LCMHELPER_INVALID_PARTIALCONFIG_INCONSISTENCY 1521
#define ID_LCMHELPER_INVALID_PARTIALCONFIG_NOTINMETACONF 1522
#define ID_LCMHELPER_ERROR_PARTIALCONFIG_UNDEFINED 1523
#define ID_LCM_PARTIALCONFIG_CONFIGURATIONNAME_MISSING 1524
#define ID_LCM_PARTIALCONFIG_MERGED_VALIDATION_FAILED 1525
#define ID_LCM_NON_TERMINATING_ERROR 1526
#define ID_MODMAN_PARTIALCONFIG_DUPLICATE_EXCLUSIVERESOURCE 1527
#define ID_MODMAN_INVALID_PARTIALCONFIG_CONFIGSOURCE 1528
#define ID_MODMAN_PARTIALCONFIG_EXCLUSIVERESOURCE_DISOBEYED 1529
#define ID_LCM_WRITEMESSAGE_SAVETOPARTIAL 1530
#define ID_LCMHELPER_DEPENDSONFILEDOESNTEXIST_MESSAGE 1531
#define ID_LCMHELPER_APPLYPARTIALCONFIG_FAILED_WITHERROR 1532
#define ID_PARTIALCONFIG_NOPARTIALCONFIGPRESENT 1533
#define ID_PARTIALCONFIG_FAILEDPARTIALCONFIGS 1534
#define ID_LCM_INVALID_RESOURCEINSTANCE 1535
#define ID_LCM_MODULENAME_NOTFOUND 1536
#define ID_PARTIALCONFIG_INVALID_EXCLUSIVERESOURCESTRING 1537
#define ID_LCM_PARTIALCONFIG_DELETINGFILE_WARNING 1538
#define ID_LCM_PARTIALCONFIG_SKIPFILE_WARNING 1539
#define ID_PARTIALCONFIG_STORECANNOTBE_CREATED 1540

/* Web pull client take IDs from 1601 - 1700*/
#define ID_PULL_CONFIGURATIONIDNOTSPECIFIED 1601
#define ID_PULL_INVALIDCONFIGURATIONIDFORMAT 1602
#define ID_PULL_INVALIDURLINCUSTOMDATA 1603
#define ID_PULL_GETACTIONFAILED 1604
#define ID_PULL_GETACTIONUNEXPECTEDRESULT 1605
#define ID_PULL_UNSECURECONNECTIONNOTALLOWED 1606
#define ID_PULLGETCONFIGURATIONFAILED 1607
#define ID_PULL_CONFIGURATIONSAVEFAILED 1608
#define ID_PULLGETCONFIGURATION_BADRESPONSE 1609
#define ID_PULLGETCONFIGURATION_NULLCHECKSUM 1610
#define ID_PULLGETCONFIGURATION_NULLCHECKSUMALGORITHM 1611
#define ID_PULLGETCONFIGURATION_INVALIDCHECKSUMALGORITHM 1612
#define ID_PULLGETCONFIGURATION_CHECKSUMSAVEFAILED 1613
#define ID_PULLGETACTION_BADRESPONSE 1614
#define ID_PULL_CHECKSUMMISMATCH 1615

#define ID_PULL_DSCCONF_NOTOPENABLE            1699
#define ID_PULL_DSCCONF_NOTREADABLE            1698
#define ID_PULL_DSCCONF_INVALIDVALUE           1697
#define ID_PULL_SSLCIPHERLISTTOOLONG           1696
#define ID_PULL_NOCONFIGDOWNLOADMANAGERS       1695
#define ID_PULL_TOOMANYCONFIGDOWNLOADMANAGERS  1694
#define ID_PULL_NOSERVERURL                    1693
#define ID_PULL_CURLFAILEDTOINITIALIZE         1692
#define ID_PULL_CURLFAILEDTOSETCIPHERLIST      1691
#define ID_PULL_CURLFAILEDTOSETNOSSLV3         1690
#define ID_PULL_CURLPERFORMFAILED              1689
#define ID_PULL_INVALIDRESPONSEFROMSERVER      1688
#define ID_PULL_INVALIDCHECKSUMALGORITHM       1687
#define ID_PULL_NOPARTIALCONFIGS               1686
#define ID_PULL_NOCONFIGURATIONSOURCE          1685
#define ID_PULL_SERVERHTTPERRORCODE            1684
#define ID_PULL_SERVERHTTPERRORCODEMODULE      1683
#define ID_PULL_INSTALLMODULEFAILED            1682
#define ID_PULL_INITIALIZEMODULETABLEFAILED    1681
#define ID_PULL_INVALIDMODULEVERSION           1680
#define ID_PULL_INSTALLMODULEANDREMOVEMODULEFAILED 1679
#define ID_PULL_RESTARTINGSERVER 1678
#define ID_PULL_CABUNDLETOOLONG 1677
#define ID_PULL_CABUNDLENOTSUPPORTED 1676
#define ID_APPLYCONFIG_SET 1675
#define ID_APPLYCONFIG_TEST 1674
#endif //__RESOURCES_LCM_H_
