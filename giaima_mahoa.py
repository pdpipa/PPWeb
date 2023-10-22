import getopt
import os
import sys
try:
	import pyzstd
	import colorama
except:
	os.system('pip install pyzstd')
	os.system('pip install colorama')
	import pyzstd
	import colorama
	os.system("cls")

ZSTD_DICT = b'7\xa40\xec\xe7UC\x0bM\x10@\xae\xa6\xe9P\xaa\xffPL\x8d\xe1Tn)\xb7Dr\xbb\xecH\xaclT)(((((\xa0\xa2\xa0CU(G\x01\x18\x08r\x18\x11\x11\x9a]k\xd3\x8a:\x16\xa9\x89\xe8%\xc2\xde{\xef\xbd\xa5\x8e\xae\xdb2\xaa\x8ee\x99\x85a\xf0\xf9\xf1#\x9b\x02\x83\x05\x19\x0c\x08\x06\x05b\xa1`\x96\xc6\x81\xac}\x04D\xe4\xe1\xa4\xc3\x01\xe2`A\xc1\xe0`\xc1\xa0\xc0\xa0`0\x10\x08\x03\xc3\xc0@(\x10\x06\x80\xc2\xc2@ \x1c\n\x07D\x82\xf48\xe9\x96\x1b\x00\xd4\x0e\x11\x06\x1d\x8bA\x901\xc6\x18bH\x19\x00 \x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x08\x00\x00\x00mName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="skillCombineLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="skillCombineSrcId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSkillMark" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration14" eventType="HitTriggerDuration" guid="38f874e2-e64b-478d-be55-fc7453046e1c" enabled="true" refParamName="" useRefParam="false" r="0.183" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="8" guid="1b06b263-6aa9-4007-a2cb-116a920b9312" status="true"/>\n\t\t\t<Event eventName="HitTriggerDuration" time="0.200" lenid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack0" eventType="StopTrack" guid="8013dc81-a485-4567-bc08-9e0ec7d7cd99" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.017" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="4" guid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack1" eventType="StopTrack" guid="8633109d-53e5-4931-87b1-bf3472773aed" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.633" exe\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe8\xb0\xa6\xe8\xae\xa9"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe6\x94\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x87\xaa\xe6\x9d\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe9\x99\xa4\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="Buff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x81\xa2\xe5\xa4\x8dBuff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe5\xb0\x84\xe7\xa8\x8b"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="CheckSkillCombineConditionTick1" eventType="CheckSkillCombineConditionTick" guid="bc7f4540-c6d9-4813-88cb-990e1d8abf7f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.433" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentBuffId" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="skillCombineId" value="136001" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType"ame="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidMoveButRotate" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<int name="rotateSpeed" value="720" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t</Event>\r\n\t\t</Track>\r\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="4abae504-d3a2-4370-a0a8-255fde6c84d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true" />\r\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="0.500" isDuration="true">\r\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<String name="clipName" value="Hit" refP/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00\xbb\x01\x00\x00J\x00\x00\x00\x17\x00\x00\x00Terms_Of_Service_Title\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x1c\x00\x00\x00\xc4\x90i\xe1\xbb\x81u kho\xe1\xba\xa3n d\xe1\xbb\x8bch v\xe1\xbb\xa5\x00=\x00\x00\x00\xe0\xb9\x80\xe0\xb8\x87\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x84\xe0\xb8\x82\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\x00\x11\x00\x00\x00\xec\x84\x9c\xeb\xb9\x84\xec\x8a\xa4 \xec\x95\xbd\xea\xb4\x80\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x12\x00\x00\x00Ketentuan Layanan\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe5\x88\xa9\xe7\x94\xa8\xe8\xa6\x8f\xe7\xb4\x84\x00g\x13\x00\x00K\x00\x00\x00\x16\x00\x00\x00Terms_Of_Service_Text\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\xe5\x85\xa7\xe5\xae\xb9\xe5\x85\xa7\xe5\xae\xb9\xe5\xbc\x89"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="collisionCheckDistanceOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="collisionCheckWidth" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInteruptOtherMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bProtectInteruptedByOtherMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsAreaLimitedToBeMoveDone" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="d7e3a6f9-943b-4dda-9650-7a88a29698f8" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.783" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnObjectDuration" time="0.233" length="0.300" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="parentId" ob\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00^KL\x00\x14\x00\x00\x000AF0A00F2605E9BB_##\x00\x00\x00\x14\x00\x00\x00349C21E70FD859FE_##\x00\x01\x00\x00\x00\x00\xe7.\x00\x00\x01\x00\x00\x00\x00\x04\x04\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00\x90\x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\n\x00\x00\x00}\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa0\x00\x00\x00\x00\xbc\x96\x98J\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00`KL\x00\x14\x00\x00\x00B8FA881B79F41C0F_##\x00\x00\x00\x14\x00\x00\x0085F89A39568DD08B_##\x00\x01\x00\x00\x00\x00`KL\x00\x01\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00b\x00\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0f\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x01\x00\x00_KL\x00\x14\x00\x00\x004BF61216E72F555D_##\x00\x00\x00\x14\x00\x00\x00EA1631C678E20D11_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00starguardcard.png\x00\x04\x16\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x002\x00\x00\x00\xfa\x00\x00\x00d\x00\x00\x00d\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x80A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x01\x00\x00@\x85:\xe1\\\x12\x00\x00@\xeb<\r\xa5\x12\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00\x05^\x0c\x00\x14\x00\x00\x00DEC1050D07839DB7_##\x00\x00\x00\x14\x00\x00\x00F620F03B6DE88773_##\x00\x01\x00\x00\x00\x00\xfa\x97\x04\x00\x01\x00\x00\x00\x00\x04\n\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00 \x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\xa4\x04\x00\x00 \x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x00\x00\xd2B\x00\x00\x80?\x00\x00\x00\x00\x00\x00\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\x87\xb4\xe5\x91\xbd\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe7\xa6\x81\xe7\x94\xa8\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe8\x83\xbd\xe9\x87\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\xa4\xe7\x94\xb2\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb\xe5\xb8\xa6\xe6\xb3\x95\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2\xef\xbc\x88\xe7\xa6\x81\xe6\xad\xa2\xe4\xbd\xbf\xe7\x94\xa8\xef\xbc\x89"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x83\xbd\xe9\x87\x8f\xe5\x8d\xe7\xba\xbf\xe5\x8e\x8b\xe5\x8a\x9b\xef\xbc\x9b\\n\\n\xe2\x80\xa6\xe2\x80\xa6\\n\\n\xe4\xba\xba\xe7\xb1\xbb\xe7\x9a\x84\xe5\xbc\xba\xe8\x80\x85\xe4\xbb\xac\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x86\xe5\x90\x84\xe8\x87\xaa\xe4\xb8\xba\xe6\x88\x98\xe7\x9a\x84\xe6\x97\xa5\xe5\xad\x90\xef\xbc\x8c\xe4\xbb\x96\xe4\xbb\xac\xe8\x81\x9a\xe9\x9b\x86\xe5\x9c\xa8\xe8\x90\xa8\xe5\xb0\xbc\xe7\x9a\x84\xe9\xba\xbe\xe4\xb8\x8b\xef\xbc\x8c\xe5\xb0\x86\xe4\xb8\x80\xe8\x82\xa1\xe8\x82\xa1\xe5\xbe\xae\xe5\xb0\x8f\xe7\x9a\x84\xe5\x8a\x9b\xe9\x87\x8f\xef\xbc\x8c\xe8\x81\x9a\xe5\x90\x88\xe6\x88\x90\xe6\x8e\xa8\xe5\x8a\xa8\xe5\x8e\x86\xe5\x8f\xb2\xe7\x9a\x84\xe6\xb4\xaa\xe6\xb5\x81\xe3\x80\x82\xe5\x9c\xa8\xe8\xbf\x99\xe8\x82\xa1\xe6\xb4\xaa\xe6\xb5\x81\xe9\x9d\xa2\xe5\x89\x8d\xef\xbc\x8c\xe5\xbc\xba\xe5\xa4\xa7\xe7\x9a\x84\xe6\x81\xb6\xe9\xad\x94\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x80\xe5\xae\x88\xe6\xb7\xb1\xe6\xb8\x8a\xef\xbc\x8c\xe7\x8b\x82\xe9\x87\x8e\xe7\x9a\x84\xe5\x85\xbd\xe7\xbe\xa4\xe5\xad\xa6\xe4\xbc\x9a\xe4\xba\x86\xe8\x87\xaa\xe6\x88\x91\xe6\x94\xb6\xe6\x95\x9b\xef\xbc\x8c\xe5\xb0\xb1\xe8\xbf\x9e\xe5\x9c\xa3\xe6\xae\xbf\xe7\x9a\x84\xe7\xa5\x9e\xe7\xa5\x87\xe4\xbb\xac\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe7\x9b\xb4\xe6\x8e\xa0\xe9\x94\x8b\xe8\x8a\x92\xe3\x80\x82\xe4\xbd\x86\xe8\x90\xa8\xe5\xb0\xbc\xe5\xb9\xb6\xe6\xb2\xa1\xe6\x9c\x89\xe8\xa2\xab\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe4\xbc\x9f\xe5\xa4\xa7\xe5\x8a\x9f\xe7\xbb\xa9\xe5\x86\xb2\xe6\x98\x8f\xe5\xa4\xb4\xe8\x84\x91\xef\xbc\x8c\xe4\xbb\x96\xe6\x97\xb6\xe5\x88\xbb\xe4\xbf\x9d\xe6\x8c\x81\xe7\x9d\x80\xe8\xad\xa6\xe6\x83\x95\xef\xbc\x8c\xe5\x8f\xaa\xe8\xa6\x81\xe6\x88\x98\xe6\x96\x97\xe7\x9a\x84\xe5\x8f\xb7\xe8\xa7\x92\xe5\x90\xb9\xe5\x93\x8d\xef\xbc\x8c\xe4\xbb\x96\xe5\xb0\xb1\xe4\xbc\x9a\xe5\x86\x8d\xe6\xac\xa1\xe6\x8c\xba\xe5\x89\x91\xe8\x80\x8c\xe4\xb8\x8a\xe3\x80\x82\\n\\n\xe2\x80\x9c\xe5\x90\xbe\xe6\x89\xa7\xe5\x90\xbe\xe5\x89\x91\xef\xbc\x8c\xe6\x96\xa9\xe5\xb0\xbd\xe5\xa5\xb8\xe9\x82\xaa\xef\xbc\x81\xe2\x80\x9d\r\n0588A320CABA3789_## = \xe7\x81\xb5\xe7\x81\xb5\xe4\xb8\xba\xe4\xbb\x80\xe4\xb9\x88\xe6\x98\xaf\xe7\x88\x86\xe7\x82\xb8\xe5\xa4\xb4\xef\xbc\x9f\r\n0590EDDF3CC30F2A_## = \xe5\xb9\xb4\xe8\xbd\xbb\xe4\xba\xba\xef\xbc\x8c\xe4\xbd\xa0\xe7\x9a\x84\xe8\xaf\x9a\xe6\x84\x8f\xe6\x89\x93\xe5\x8a\xa8\xe4\xba\x86\xe6\x88\x91\\n\xe5\xa6\x82\xe6\x9e\x9c\xe4\xbd\xa0\xe4\xb8\x8d\xe4\xbb\x8b\xe6\x84\x8f\xe5\x92\x8c\xe6\x88\x91\xe4\xb8\x80\xe8\xb5\xb7\\n\xe8\xa1\x8c\xe4\xbe\xa0\xe6\xad\xa3\xe4\xb9\x89\xef\xbc\x8c\xe9\x99\xa4\xe6\x81\xb6\xe6\x89\xac\xe5\x96\x84\\n\xe5\x88\x9a\xe5\xa5\xbd\xe6\x88\x91\xe7\x8e\xb0\xe5\x9c\xa8\xe7\xbc\xba\xe4\xb8\x80\xe4\xb8\xaa\xe5\x8a\xa9\xe7\x90\x86\\n\xe4\xbb\x8a\xe5\x90\x8e\xe6\x88\x91\xe4\xbb\xac\xe5\xb0\xb1\xe6\x98\xaf\xe6\x97\xa0\xe6\x95\x8c\xe7\x9a\x84\xe9\x9c\xb9\xe9\x9b\xb3\xe7\xbb\x84\xe5\x90\x88\xef\xbc\x81\r\n0592D198A67E021F_## = <color=#ffd200>\xe8\xa7\xa3\xe9\x94\x81\xe6\x9d\xa1\xe4\xbb\xb6</color>\xef\xbc\x9a\xe4\xb8\x8e<color=#ffd200>{0}</color>\xe8\xbe\xbe\xe5\x88\xb0<color=#ffd200>\xe7\xbe\x81\xe7\xbb\x8a\xe9\x98\xb6\xe6\xae\xb52 \xe7\x9b\xb8\xe8\xaf\x86</color>\r\n05A181D7672725DC_## = \xe6\xb4\x9b\xe9\x87\x8c\xe6\x98\x82\r\n05A9BBD41D0A9179_## = \xe2\x80\x9c\xe4\xb9\x9d\xe5\xa4\xa9\xe4\xb9\x8b\xe4\xb8\x8a\xef\xbc\x8c\xe7\xa5\x9e\xe5\xba\xa7\xe4\xb9\x8b\xe6\x97\x81\xef\xbc\x8c\xe5\x85\xad\xe7\xbf\xbc\xe8\x88\x9e\xe5\x8a\xa8\xef\xbc\x8c\xe4\xbb\xa5\xe7\xbf\xb1\xe4\xbb\xa5\xe7\xbf\x94\xe3\x80\x82\xe2\x80\x9d\\n\\n\xe8\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x97\x8b\xe8\xbd\xac"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="materialParentActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyScaling" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableLayer"head145.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x15\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00:\x00\x00\x00\x0f\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x16\xf6\x99\x00\x0c\x00\x00\x00vp10042.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00X\x00\x00\x00\x0f\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x17\xf6\x99\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x18\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x01\x00\x00\x00\x00O\x00\x00\x00\x0f\x00\x00\x00\n\x00\x00\x00\xab\x9e\x98\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x19\xf6\x99\x00\x12\x00\x00\x00return_js_new.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1a\xf6\x99\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1b\xf6\x99\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1c\xf6\x99\x00\x0c\x00\x00\x00vp90007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1d\xf6\x99\x00\x0c\x00\x00\x00vp10106.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00>\x00\x00\x00\x0f\x00\x00\x00\x0f\x00\x00\x00\xac\x9e\x98\x00\x0c\x00\x00\x00vp90005.png\x00\x1e\xf6\x99\x00\x10\x00\x00\x00valorpass03.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1f\xf6\x99\x00\x0c\x00\x00\x00vp12007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00 \xf6\x99\x00\x0c\x00\x00\x00vp11029.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00!\xf6\x99\x00\r\x00\x00\x00vp120100.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00Q\x00\x00\x00\x0f\x00\x00\x00\x14\x00\x00\x00\xad\x9e\x98\x00\x0c\x00\x00\x00vp90007.png\x00#\xf6\x99\x00\x14\x00\x00\x00level20skin_big.png\x00\x01\x00\x00\x00\x00\x10\x00\x00\x00level20skin.png\x00;\x00\x00\x00\x0f\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\xe7\x8e\x84\xe7\xad\x96\xe8\xa2\xab\xe5\x8a\xa8\x00\x16\x00\x00\x00\xe5\x87\xbb\xe6\x9d\x80\xe6\x88\x96\xe5\x8a\xa9\xe6\x94\xbb\xe8\x8b\xb1\xe9\x9b\x84\x007\x00\x00\x00Prefab_Characters/Prefab_Hero/195_BaiLiXuanCe/skill/P2\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xbe\x00\x00\x00(<\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\xe5\x8f\xb6\xe5\xa8\x9c\xe5\xad\xa6\xe4\xb9\xa0\xe5\xa4\xa7\xe6\x8b\x9b\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x004\x00\x00\x00Prefab_Characters/Prefab_Hero/154_HuaMuLan/skill/P1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xce\x00\x00\x00%\xd5\x01\x00\xd0\x07\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00[EX]\xe7\x99\xbd\xe8\xb5\xb7\xe8\xa2\xab\xe5\x8a\xa8\x00\x13\x00\x00\x00\xe5\x8f\x97\xe5\x87\xbb\xe6\x9c\x89\xe5\x87\xa0\xe7\x8e\x87\xe8\xbd\xac\x00:\x00\x00\x00Prefab_Characters/Prefab_Hero/120_BaiQi/skill/extend/exP1\x00\x02\x00\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\xbf\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\xe7\xba\xb3\xe5\x85\x8b\xe7\xbd\x97\xe6\x96\xaf\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/150_HanXin/skill/extend/exP2\x00\x08\x00\x00\x00\xa0\x0f\x00\x00\x14\x00\x00\x00\xf4\x01\x00\x00\x8c\x06\x17\x00\x98:\x00\x00\x0c\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x12\x01\x00\x00>A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00\xef\xbc\x8810v10\xef\xbc\x89\xe7\x8c\xb4\xe5\xad\x90\xe6\xaf\x8f\xe6\xac\xa1\xe9\x87\x8a\xe6\x94\xbe\xe6\x8a\x80\xe8\x83\xbd\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xe5\xb0\x86\xe4\xbc\x9a\xe8\x8e\xb7\xe5\xbe\x97\xe4\xb8\x80\xe4\xb8\xaa\xe6\x8a\xa4\xe7\x9b\xbe\xef\xbc\x8c\xe5\x8f\xaf\xe5\x8f\xa0\xe5\x8a\xa05\xe6\xac\xa1\x00\x12\x00\x00\x00\xe6\x82\x9f\xe7\xa9\xba[EX]\xe8\xa2\xab\xe5\x8a\xa81\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/167_WuKong/skill/extend/exP1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00e="" r="0.517" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CameraShakeDuration" time="2.000" length="2.000" isDuration="true">\n\t\t\t\t<bool name="useMainCamera" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="shakeRange" x="0.500" y="0.500" z="0.500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_self" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_target" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_enemy" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_allies" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useAccumOffset" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cosDecay" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="cosDecayFactor" v\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00M\x00\x00\x00\x1f\xb2\x01\x00%\x00\x00\x00Play_SunShangXiang_VO_TiaoXin_Skin13\x00i+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00J\x00\x00\x00)\xb2\x01\x00"\x00\x00\x00Play_sunshangxiang_tiaoxin_Skin14\x00j+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00\x85\xb5\x01\x00\x18\x00\x00\x00Play_GongShuBan_TiaoXin\x00\xc0+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\x99\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin2\x00\xc2+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xb7\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin5\x00\xc5+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xc1\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin6\x00\xc6+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00m\xb9\x01\x00\x18\x00\x00\x00Play_ZhuangZhou_TiaoXin\x00$,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00=\x00\x00\x00U\xbd\x01\x00\x15\x00\x00\x00Play_LiuShan_TiaoXin\x00\x88,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00?\x00\x00\x00=\xc1\x01\x00\x17\x00\x00\x00Play_GaoJianLi_TiaoXin\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00Q\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin2\x00\xee,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00[\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin3\x00\xef,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00<\x00\x00\x00%\xc5\x01\x00\x14\x00\x00\x00Play_JingKe_TiaoXin\x00P-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00M\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin4\x00T-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00W\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin5\x00U-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00C\x00\x00\x00o\xc6\x01\x00\x1b\x00\x00\x00Plname="bInverse" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupActorType" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupRadius" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterInTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="teamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="diffTeamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="monsterTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="soldierTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetBehaviourModeTick0" eventType="SetBehaviourModeTick" guid="53e062a5-ebd1-4b49-83fe-4b2026e48ae4" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.283" exe\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bChargingEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="chargingDistance" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="distance" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bResetMoveDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="minSpeed" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="12000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groundOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreHeight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="acceleration"v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/skill1_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_organ/tower/skill1_bullet_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/makeDamage2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00*\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc3\x00\x00\x00\x02\x00\x00\x00r\x00\x00\x00\x06\x00\x00\x00v1`\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String2\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/A1E2\x04\x00\x00\x00\x04\x00er/New_BlueTower/skill/New_BlueTower_makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00L\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe5\x00\x00\x00\x02\x00\x00\x00\x94\x00\x00\x00\x06\x00\x00\x00v1\x82\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringT\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_BlueTower/skill/New_BlueTower_A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75001\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xad\x03\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x1d\x03\x00\x00\x03\x00\x00\x00\x07\x01\x00\x01\x00\x00\x00\x00\x00\r\x00\x00\x00\xe5\xa4\xa7\xe7\xa5\x9e\xe5\x85\xb3\xe5\x8d\xa1\x00\x15\x00\x00\x00Tutorial_BGod_Design\x00\x17\x00\x00\x00ART_5V5_01_High_Artist\x00\x0c\x00\x00\x00PVP_5V5_Nav\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00~\x02\x00\x00z\x02\x00\x00{\x02\x00\x00\x7f\x02\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00t\x02\x00\x00w\x02\x00\x00x\x02\x00\x00\x80\x02\x00\x00\x81\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00\x00\x007\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x08\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x00\x00pvp_5_small\x00\r\x00\x00\x00pvp_5_detail\x00\n\x00\x00\x00pvp_5_big\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xdd\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x02\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00Play_PVP_Music\x00\x0f\x00\x00\x00Stop_PVP_Music\x00\x01\x00\x00\x00\x00\n\x00\x00\x00Music_PVP\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90_\x01\x00\x95_\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x02\x00\x00e\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x10\x00\x00\x00\xe5\x8f\xac\xe5\x94\xa4\xe5\xb8\x88\xe6\x88\x98\xe5\x9c\xba\x00\x15\x00\x00\x00PVE_1_1_logic_Design\x00\x18\x00\x00\x00ART_PJGC_02_High_Artist\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00Img_Story\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x03\x00\x00\x00\xf3\x03\x00\x00\xf4\x03\x00\x00\xf5\x03\x00\x00Q\xc3\x00\x00\x00\x00\x00\x00f\x00\x00\x00\x05M\x04\x00\x00\x05\xb1\x04\x00\x00\x05\x15\x05\x00\x00\x05{\x05\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\t\x00\x00\x00\r\x00\x00\x00F\x05\x00\x00\xe7\x06\x00\x00\x88\x08\x00\x00\x9e\t\x00\x00\x84\x03\x00\x00\x9a\x04\x00\x00\xb0\x05\x00\x00i\x06\x00\x00\x00\x08\x00\x00\x00PVE_1_3\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa*\x00\x00\x00\x00\x00\x00\xc9\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00o\x00\x00\x00y\x00\x00\x00\x83\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 N\x00\x00\x00\x00\x00\x00\x0ee\x00\x01\x00\x00\x00\x00E\x00\x00\x00f\x82\x17\x00\x19\x00\x00\x00Play_Yena_VOX_Come_Skin7\x00/<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00@\x00\x00\x00\xba\xa6\x17\x00\x14\x00\x00\x00Play_LuoBin_VO_Come\x00\x8c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00D\x00\x00\x00\xca\xcd\x17\x00\x18\x00\x00\x00Play_ZhangLiang_VO_Come\x00\xf0<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00\xf6\xce\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin3\x00\xf3<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00Z\xcf\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin4\x00\xf4<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00A\x00\x00\x00\xda\xf4\x17\x00\x15\x00\x00\x00Play_BuZhiHuoWu_Show\x00T=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\x06\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin3\x00W=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00j\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin4\x00X=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\xce\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin5\x00Y=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x002\xf7\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin6\x00Z=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00)\x00\x00\x00\xea\x1b\x18\x00\x01\x00\x00\x00\x00\xb8=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00)\x00\x00\x00\nj\x18\x00\x01\x00\x00\x00\x00\x80>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00*\xb8\x18\x00\x16\x00\x00\x00Play_Nakelulu_VO_Come\x00H?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00V\xb9\x18\x00\x1c\x00\x00\x00Play_Nakelulu_VO_Come_Skin3\x00K?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00:\xdf\x18\x00\x1c\x00\x00\x00Play_163_JuYouJing_VOX_Come\x00\xac?\x00\x01\x00\x00\x00\x00\x00?\x00\x00\x00Prefab_Skill_Effects/Level_Effects/AutoChess_Effects/ChessDrop\x00\x00\x00\x80?\x01\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MSES\x07\x00\x00\x00\x17\x00\x00\x00\x0f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005d388e873657b33c203ea1a6adbbd555\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x001131\x00\x02\x00\x00\x00P\x00\x13\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x001132\x00\x02\x00\x00\x00B\x00\x12\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00901\x00\x02\x00\x00\x00C\x00\x12\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00902\x00\x02\x00\x00\x00D\x00\x13\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x001130\x00\x02\x00\x00\x00E\x00\x13\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x001133\x00\x02\x00\x00\x00F\x00\x13\x00\x00\x00\x07\x00\x00\x00\x05\x00\x00\x001134\x00\x02\x00\x00\x00G\x00\x13\x00\x00\x00\x08\x00\x00\x00\x05\x00\x00\x001135\x00\x02\x00\x00\x00H\x00\x13\x00\x00\x00\t\x00\x00\x00\x05\x00\x00\x001136\x00\x02\x00\x00\x00I\x00\x13\x00\x00\x00\n\x00\x00\x00\x05\x00\x00\x001137\x00\x02\x00\x00\x00J\x00\x13\x00\x00\x00\x0b\x00\x00\x00\x05\x00\x00\x001138\x00\x02\x00\x00\x00K\x00\x13\x00\x00\x00\x0c\x00\x00\x00\x05\x00\x00\x001139\x00\x02\x00\x00\x00L\x00\x13\x00\x00\x00\r\x00\x00\x00\x05\x00\x00\x001180\x00\x02\x00\x00\x00M\x00\x13\x00\x00\x00\x0e\x00\x00\x00\x05\x00\x00\x001181\x00\x02\x00\x00\x00N\x00\x13\x00\x00\x00\x0f\x00\x00\x00\x05\x00\x00\x001183\x00\x02\x00\x00\x00O\x00MSES\x07\x00\x00\x00\x82\x01\x00\x00a\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e7c2b766e9bca08f64db4f0b283f3ce4\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xd6\x00\x00\x00i\x00\x00\x00\x14\x00\x00\x0096C81CC5CA834D6C_##\x00\x1f\x00\x00\x00WrapperAI/Hero/HeroAutoChessAI\x00\xa0(\x00\x00\x00\x00\x00\x00LO\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00$\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Born\x00\x01\x00\x00\x00\x00)\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Dead_Born\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x00\x00\x00j\x00\x00\x00\x14\x00\x00\x000D17FEB38CC06\x00\x00\x00\x04\x00\x00\x00&\x01\x00\x00\x12\x00\x00\x00iCollisionSize&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00x9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V500\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00z9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/542_Tachi/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/542_Tachi/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xab%\xb5\xdc\x86\x1c\x00\x00\x86\x1c\x00\x00/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81^\x00\x00\x00Prefab_Hero/542_Tachi/542_Tachi_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xdb\x00\x00\x001\x1d\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00121_MiYue/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00121_MiYue/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00121_MiYue/skill/AutoChess/PK\x03\x04RefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAlwaysLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="b1stTickParentRot" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHideWhenDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreWhenHideModel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUse3DUICamerang name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRefreshVision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidTargetOutOfNavmeshConvexHull" va\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x06\x05\x00\x00\x04\x00\x00\x00\x1e\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb7\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00F\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdf\x00\x00\x00\x02\x00\x00\x00\x8e\x00\x00\x00\x06\x00\x00\x00v1|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00M\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe6\x00\x00\x00\x02\x00\x00\x00\x95\x00\x00\x00\x06\x00\x00\x00v1\x83\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringU\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack02_spell01\x04\x00\x00P\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x004EEC4F2E66D84324_##\x00\x14\x00\x00\x0022CA5E1185A20996_##\x00\n\x00\x00\x0011084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa2\x00\x00\x00\\R\x00\x00\x02\x00\x01\x01=\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/kill/Kill_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x009C5DF28AAE7D3EE2_##\x00\x14\x00\x00\x00D24D8A620C89E63A_##\x00\n\x00\x00\x0021084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa6\x00\x00\x00ly\x00\x00\x03\x00\x01\x01A\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00849FC2788990326B_##\x00\x14\x00\x00\x00E94BDB26D3AF7FEB_##\x00\n\x00\x00\x0031084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa5\x00\x00\x00M+\x00\x00\x01\x00\x01\x01@\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/returncity/return_5V5_01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00ACA13FE146E55BC7_##\x00\x14\x00\x00\x00F3CFA939C7E48289_##\x00\n\x00\x00\x0011085.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc9\x00\x00\x00*\xa0\x00\x00\x04\x00\x01\x011\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_houyi_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x009DF7DA730FC32408_##\x00\x14\x00\x00\x00559A118E1D79C256_##\x00\n\x00\x00\x0041002.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc7\x00\x00\x00+\xa0\x00\x00\x04\x00\x01\x01/\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_jin_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x0084D3846A3B38B40D_##\x00\x14\x00\x00\x00D3B4AFBD692854AB_##\x00\n\x00\x00\x0041003.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc8\x00\x00\x00,\xa0\x00\x00\x04\x00\x01\x010\x00\x00\x00Prefngle name="randRotEnd" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="7d755f67-9943-4d08-b439-ce9215f3a028" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.417" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnBulletTick" time="0.200" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetPosActorId" objectName="None" id="-1" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="referenceObjectId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="ActionName" value="prefab_characters/prefab_hero/190_zhugeliang/skill/AutoChess/aca1b1" refvalue="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpecialBuffEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bActionCtrlObjs" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleTeamNotSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="MoveBulletDuration0" eventType="MoveBulletDuration" guid="a4b4420f-87ae-4a8f-8c74-f5b800394aec" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.367" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="MoveBulletDuration" time="0.000" length="0.533" isDpeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50002\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50000\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xe4\x01\x00\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00L\x01\x00\x00\x01\x00\x00\x00D\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdd\x00\x00\x00\x02\x00\x00\x00\x8c\x00\x00\x00\x06\x00\x00\x00v1z\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/Common_Effects/EF_PVP_M_11DefenseTower_Blue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00)\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x8d\x02\x00\x00\x02\x00\x00\x00B\x01\x00\x00t name="\xe5\xa2\x9e\xe5\x8a\xa0\xe9\x87\x91\xe9\x92\xb1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\x8b\xb1\xe9\x9b\x84\xe7\x94\x9f\xe5\x91\xbd\xe6\x97\xb6\xe9\x95\xbf"/>\n\t\t\t\t\t<uint name="\xe7\xa6\xbb\xe5\xbc\x80\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85\xe4\xb8\x80\xe5\xae\x9a\xe8\x8c\x83\xe5\x9b\xb4\xe5\x90\x8e\xe6\xb8\x85\xe9\x99\xa4BUFF"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90"/>\n\t\t\t\t\t<uint name="\xe9\x99\xa4\xe7\x9b\xae\xe6\xa0\x87\xe5\xa4\x96\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe9\x80\x9f\xe6\x8a\xb5\xe6\x8a\x97"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa3\xe9\x99\xa4\xe5\x87\x8f\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\xad\xbb\xe4\xba\xa1"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe6\xb6\x88\xe8\x80\x97\xe5\x89\x8a\xe5\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\xb6\xb3\xe7\x90\x83\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe5\xa5\x89\xe7\x8c\xae"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe8\xa7\x92\xe8\x89\xb2\xe9\x87\x8d\xe7\x94\x9f"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe8\x8e\xb7\xe5\x8f\x96\xe5\x89\x8a\xe5\x87\x8f\xe6\xaf\x94\xe4\xbe\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5\xe9\x98\xb2\xe5\xbe\xa1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe4\xba\x92\xe7\x9b\xb8\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xb8\xbb\xe4\xba\xba\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe5\x8c\x96\xe7\xbb\x99\xe5\xae\xa0\xe7\x89\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x81\x90\xe6\x83\xa7\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe5\x8d\x95\xe6\xac\xa1\xe4\xbc\xa4\xe5\xae\xb3\xe4\xb8\x8a\xe4\xb8\x8b\xe9\x99\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8a\x80\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\xad"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe8\x80\x97\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc\xe6\x8a\xb5\xe6\x8c\xa1\xe4\xbc\xa4\xe5refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTargetBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTotalHitCount" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEdgeCheck" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bExtraBuff" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_1" value="505100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_2" value="505120" refPSetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetAttackDirDuration" time="0.000" length="0.050" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration0" eventType="ForbidAbilityDuration" guid="70d891be-ca4c-4c49-af6f-53ed54d35f4b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.283" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.200" isD name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x80\x92\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe7\x90\x83\xe6\xa7\xbd\xe4\xbd\x8d"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xb9\xe6\x8d\xae\xe6\x8a\xa4\xe7\x94\xb2\xe5\x80\xbc\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xbc\xe6\x8c\xa1\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\xa4\xa7\xe8\xa7\x86\xe9\x87\x8e\xe5\x8d\x8a\xe5\xbe\x84"/>\n\t\t\t\t\t<uint name="\xe5\x8d\x95\xe4\xb8\xaa\xe6\x8a\x80\xe8\x83\xbd\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\xbc\xb9"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe5\xa4\x8d\xe6\xb4\xbb\xe6\x97\xb6\xe9\x97\xb4"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\xa7\x92\xe8\x89\xb2\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\xa7\xbd\xe4\xbd\x8d\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe9\x95\xbf\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe6\x8d\xa2"/>\n\t\t\t\t\t<uint name="\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xae\xad\xe8\xaf\xab\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe9\x94\x90\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\x87\xbb\xe6\x99\xae\xe6\x94\xbb\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe5\x8f\x97\xe5\x88\xb0\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe9\x80\xa0\xe6\x88\x90\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x83\x8c\xe5\x90\x8e\xe6\x94\xbb\xe5\x87\xbb\xe6\x9a\xb4\xe5\x87\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87\xe8\xbd\xac\xe5\x8c\x96\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3 name="excuteMoveCmd" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="immediaRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayMSES\x07\x00\x00\x00\x08\x00\x00\x00\x10\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000ed9c5e8c7fd9b42e102b09260202589\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00`\xea\x00\x00\x04\x00\x00\x00a\xea\x00\x00\x04\x00\x00\x00b\xea\x00\x00\x04\x00\x00\x00c\xea\x00\x00\x04\x00\x00\x00d\xea\x00\x00\x04\x00\x00\x00e\xea\x00\x00\x04\x00\x00\x00f\xea\x00\x00\x04\x00\x00\x00g\xea\x00\x00\x04\x00\x00\x00h\xea\x00\x00\x04\x00\x00\x00i\xea\x00\x00\x04\x00\x00\x00j\xea\x00\x00\x04\x00\x00\x00k\xea\x00\x00\x04\x00\x00\x00l\xea\x00\x00\x04\x00\x00\x00m\xea\x00\x00\x04\x00\x00\x00n\xea\x00\x00\x04\x00\x00\x00o\xea\x00\x00MSES\x07\x00\x00\x00\xb6\x00\x00\x00\x00\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0024e234988d548d1822de209cfbd17add\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00|\x01\x00\x00\xe9\x03\x00\x00\x05\x00\x00\x00Body\x00\x05\x00\x00\x00Hair\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_512.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_512_Mask.bytes\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_256.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_256_Mask.bytes\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00x\x01\x00\x00\xea\x03\x00\x00\x05\x00\x00\x00Body\x00\x01\x00\x00\x00\x00O\x00\x00\x00ChParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSpecifiedDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="specifiedDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReachDestStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bStopOnNavEdge" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDelayLeave" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="randomRotateRange" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepRelateDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOptimizeLanding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontFallInWall" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration1" eventType="HitTriggerDuration" guid="ed80eb7a-cbd8-4b36-a5da-860e3ab6f453" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.383" exeProSmall" type="int" value="5000" />\r\n    <par name="c_HideContinueSelfHP_ConSmall" type="int" value="7000" />\r\n  </pars>\r\n  <node class="SelectorLoop" version="1" id="0">\r\n    <node class="WithPrecondition" version="1" id="40">\r\n      <node class="Action" version="1" id="42">\r\n        <property Method="Self.NucleusDrive::Logic::ActorBaseAgent::IsDeadState()" />\r\n        <property PreconditionFailResult="BT_FAILURE" />\r\n        <property ResultOption="BT_INVALID" />\r\n      </node>\r\n      <node class="Sequence" version="1" id="51">\r\n        <node class="Action" version="1" id="25">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SetCurrCombatDecision(Idle,32)" />\r\n          <property PreconditionFailResult="BT_FAILURE" />\r\n          <property ResultOption="BT_INVALID" />\r\n        </node>\r\n        <node class="Action" version="1" id="41">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SwitchMicroTree(&quot;WrapperAI/Hierarchical/MicroAIs/HeroMicroIdelAI&quot;,true)" />\r\n="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceClearSkillIndicator" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="a74d46ba-4213-46ba-a7ec-e1f30bd87c8a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.917" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.400" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReturnCacheWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill1"!\x00E/\x07\xb9T\x0e\x00\x00T\x0e\x00\x00\x1d\x00\x00\x00156_ZhangLiang/skill/A4B1.xml\xef\xbb\xbf<?xml version="1.0" encoding="utf-8"?>\r\n<Project>\r\n  <TemplateObjectList>\r\n    <TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" />\r\n    <TemplateObject objectName="target" id="1" isTemp="false" />\r\n    <TemplateObject objectName="bullet" id="2" isTemp="true" />\r\n  </TemplateObjectList>\r\n  <RefParamList>\r\n    <uint name="156a4b1" value="0" refParamName="" useRefParam="false" />\r\n  </RefParamList>\r\n  <Action tag="" length="5.000" loop="false">\r\n    <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="a108b9de-b380-464d-ad3f-97838128e929" enabled="true" refParamName="" useRefParam="false" r="0.417" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="3.000" isDuration="true">\r\n        <String name="OutputLiteBulletName" value="156a4b1" refParamName="" useRefParam="false" />\r\n        <uint name="ConfigID" valisDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x80\xe8\x83\xbdCD"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe7.String\x0f\x00\x00\x00\x05\x00\x00\x00VSpell3\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\t\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xa2\x00\x00\x00\x02\x00\x00\x00Q\x00\x00\x00\x06\x00\x00\x00v1?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x11\x00\x00\x00\x05\x00\x00\x00VSpell3_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\x1c\x00\x00\x00\xe0\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0055da304ff85c361e25965639354f5378\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00%w\x00\x00rRepeatedly" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="overrideCDValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="triggerRatio" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xa0\x04\xec\x038=\x00\x008=\x00\x00\x1a\x00\x00\x00107_Zhaoyun/skill/A1E1.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="0.500" loop="false">\n\t\t<Track trackName="FilterTargetType6" eventType="FilterTargetType" guid="20f64bb4-0d0e-40ed-91b4-7ee34475407e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.083" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="FilterTargetType" timetem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/M1A2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00:\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x82\x00\x00\x00\x06\x00\x00\x00v1p\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/PassiveResource/JungleHeal\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00;\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x83\x00\x00\x00\x06\x00\x00\x00v1q\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/PassiveResource/JungleHealB1\x04\x00\x00\x00\x04\x00cts/hero_skill_effects/199_li/li_attack01_spll01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe0\x00\x00\x00\x02\x00\x00\x00\x8f\x00\x00\x00\x06\x00\x00\x00v1}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/Li_attack_spell02_trail\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdb\x00\x00\x00\x02\x00\x00\x00\x8a\x00\x00\x00\x06\x00\x00\x00v1x\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03b\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xda\x00\x00\x00\x02\x00\x00\x00\x89\x00\x00\x00\x06\x00\x00\x00v1w\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03\x04\x00\x00\x00\x04\x00em.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/999_ChessPlayer/99940_ChessPlayer_Show2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00~\x01\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\x1b\x01\x00\x00\x02\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00\xb3\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00W\x00\x00\x00\x01\x00\x00\x00O\x00\x00\x00\t\x00\x00\x00Scale:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.3\x04\x00\x00\x00\x04\x00\x00\x00i\x00\x00\x00!\x00\x00\x00bShadowCameraFollowLobbyActor<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x19\x00\x00\x00runAnimationBaseSpeed;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\r\x00\x00\x00\x05\x00\x00\x00V0.86\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V3000\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0e\x00\x00\x00LobbyScale8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00alue="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID" value="11601" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseCombo" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID1Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkillLevel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="11600" ref\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00(#\x00\x00L\x1d\x00\x00p\x17\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x02\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x10\'\x00\x00c\x00\x00\x00X\x00\x00\x00\x08\x00\x00\x00\x03\x00\r\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\xb9\xb3\xe5\x88\x86\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x88\x13\x00\x00\x01\x03\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x10\'\x00\x00{\x00\x00\x00Y\x00\x00\x00\x08\x00\x00\x00\x04\x00%\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x02\x00\x02\x00\x10\'\x00\x00p\x17\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00p\x17\x00\x00\x00\x10\'\x00\x00x\x00\x00\x00Z\x00\x00\x00\x08\x00\x00\x00\x05\x00"\x00\x00\x00\xe9\x98\xb5\xe8\x90\xa5\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x8a\xa9\xe6\x94\xbb\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00Prefab_Hero/510_Liliana/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xe9a\x8a\x18W5\x00\x00W5\x00\x003\x00\x00\x00Prefab_Hero/510_Liliana/510_Liliana_actorinfo.bytesW5\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x035\x00\x00\x0e\x00\x00\x00Y\x00\x00\x00\r\x00\x00\x00ActorName@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x12\x00\x00\x00\x05\x00\x00\x00V\xe8\x8e\x89\xe8\x8e\x89\xe5\xae\x89\x04\x00\x00\x00\x04\x00\x00\x00\xeb\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa3\x01\x00\x00\x03\x00\x00\x00\x89\x00\x00\x00\x0b\x00\x00\x00Elementr\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/510_Liliana/5101_Liliana_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x89\x00\x00\x00Param="false"/>\n\t\t\t\t<int name="iDelayDisappearTime" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\xad\xbb\xe4\xba\xa1\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb6\xe4\xbb\x96\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe6\x88\x98\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe6\x96\x97\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe9\x9d\x9e\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bExcludeSpecialActor"TPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00J\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe3\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x06\x00\x00\x00v1\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/Prefab_Soldier/New_Truck/skill/monster_atk_bullet_noaoe\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00=\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x85\x00\x00\x00\x06\x00\x00\x00v1s\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringE\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00C\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdc\x00\x00\x00\x02\x00\x00\x00\x8b\x00\x00\x00\x06\x00\x00\x00v1y\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9a\x01\x00\x00\x0c\x00\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/common_effects/allhero_jiaxue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V4\x04\x00\x00\x00\x04\x00\x00\x00>\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x86\x00\x00\x00\x06\x00\x00\x00v1t\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringF\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/526_Summoner/5261_Summoner_LOD1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00<\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x84\x00\x00\x00\x06\x00\x00\x00v1r\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Birth1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe1\x00\x00\x00\x02\x00\x00\x00\x90\x00\x00\x00\x06\x00\x00\x00v1~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Summoner_pet_death\x04\x00\x00ram="false"/>\n\t\t\t\t<bool name="bFilterSameCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlySelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyHostHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRevive" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="attackType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x89\x80\xe6\x9c\x89\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x91\xe6\x88\x98\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x9c\xe7\xa8\x8b\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bSelectJob" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="jobType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="N/A"/>\n\t\t\t\t\t<uint name="\xe5\x9d\xa6\xe5\x85\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe5\xa3\xab"/>\n\t\t\t\t\t<uint name="\xe5\x88\xba\xe5\xae\xa2"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe5\xb8\x88"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x84\xe6\x89\x8b"/>\n\t\t\t\t\t<uint name="\xe8\xbe\x85\xe5\x8a\xa9"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterGrouped" val1_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x17\x00\x00\x00ArtLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa8\x01\x00\x00\x03\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow1\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow2\x04\x00\x00\x00\x04\x00\x00\x00\x88\x00\x00\x00\x0b\x00\x00\x00Elementq\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamerao\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Cam\x04\x00\x00\x00\x04\x00\x00\x00\x0e\x18\x00\x00\x0e\x00\x00\x00SkinPrefabG\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement[]\x04\x00\x00\x00\xb1\x17\x00\x00\x03\x00\x00\x00\xc2\x07\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00j\x07\x00\x00\x06\x00\x00\x00\xe9\x01\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x9d\x01\x00\x00\x03\x00\x00\x00\x87\x00\x00\x00\x0b\x00\x00\x00Elementp\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x000986.wem\x007\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00+\x00\x00\x00Sound/Android/Chinese(Taiwan)/97838123.wem\x008\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/987101814.wem\x008\x00\x00\x00\xe4\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/994406221.wem\x008\x00\x00\x00\xe5\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995073947.wem\x008\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995257090.wem\x00$\x00\x00\x00\xe7\x00\x00\x00\x04\x00\x00\x00\x18\x00\x00\x00AssetBundle/Show/BG/*.*\x00E\x00\x00\x00\xe8\x00\x00\x00\x01\x00\x00\x009\x00\x00\x00AssetBundle/Show/Hero/133_DiRenJie_show_base.assetbundle\x00A\x00\x00\x00\xe9\x00\x00\x00\x03\x00\x00\x005\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_DiRenJie_Show.bnk\x00+\x00\x00\x00\xea\x00\x00\x00\x05\x00\x00\x00\x1f\x00\x00\x00AssetBundle/Modules/Soccer/*.*\x00-\x00\x00\x00\xeb\x00\x00\x00\x05\x00\x00\x00!\x00\x00\x00AssetBundle/Modules/FiveCamp/*.*\x00/\x00\x00\x00\xec\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_Zhaoyun_SFX.bnk\x00>\x00\x00\x00\xed\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_Zhaoyun_VO.bnk\x00/\x00\x00\x00\xee\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_XiangYu_SFX.bnk\x00>\x00\x00\x00\xef\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_XiangYu_VO.bnk\x003\x00\x00\x00\xf0\x00\x00\x00\x03\x00\x00\x00\'\x00\x00\x00Sound/Android/Hero_WangZhaoJun_SFX.bnk\x00B\x00\x00\x00\xf1\x00\x00\x00\x03\x00\x00\x006\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_WangZhaoJun_VO.bnk\x00?\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_LiuShan_SFX.bnk\x00>\x00\x00\x00\xf3\x00\x00\x00\x03\x00\x00\x00useRefParam="false"/>\n\t\t\t\t<String name="endClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayEndClipName" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTriggerTick0" eventType="ChangeSkillTriggerTick" guid="7e6b69c3-4a8c-40e5-bbc7-971898233929" enabled="true" useRefParam="false" refParamName="" r="0.800" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ChangeSkillTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="effectTime" e="\xe4\xb8\x8d\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="interuptAutoAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="a66c0c5d-659b-4258-b6f7-6630f5046041" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.117" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="taMSES\x07\x00\x00\x00}\x00\x00\x00f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e0a70c7ddff5db1861c7359c802ff1eb\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00y\x00\x00\x00\x01\x00\x00\x00\x01\x01\x14\x00\x00\x00BB2CD71CABB8E0D8_##\x00=\x00\x00\x00UGUI/Particle/UI_MapCircle_effect/UI_MapCircle_effect_Yellow\x00\x14\x00\x00\x008574E33444BD2708_##\x00\x01\x00y\x00\x00\x00\x02\x00\x00\x00\x01\x01\x14\x00\x00\x00033F49AD5A74\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00K\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe4\x00\x00\x00\x02\x00\x00\x00\x93\x00\x00\x00\x06\x00\x00\x00v1\x81\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringS\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xab\x02\x00\x00\x02\x00\x00\x00Q\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xea\x00\x00\x00\x02\x00\x00\x00\x99\x00\x00\x00\x06\x00\x00\x00v1\x87\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringY\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/chusheng_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x01\x00\x00\x0b\x00\x00\x00uncInstant0" eventType="SkillFuncInstant" guid="8d09eb2f-50ed-4358-a741-27ca7e1a94dd" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.667" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillFuncInstant" time="0.000" isDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration12" eventType="ForbidAbilityDuration" guid="ae7adc4b-a73f-4229-a4f1-dd860c67f460" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.117" b="0tion" x="0" y="0" z="1500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHeroEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseIndicatorDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="targetdir" useRefParam="true"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" vaorceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetCollisionTick" time="0.180" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="type" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="BOX"/>\n\t\t\t\t\t<uint name="SPHERE"/>\n\t\t\t\t\t<uint name="CYLINDERSECTOR"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bIsBlockMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderLine" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockJungleMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="blockCampType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x95\x8c\xe5\xaf\xb9\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe8\x87\xaa\xe5\xb7\xb1\xe9\x98\xb5\xe8\x90\xa5"22C6_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00e2\x00\x00f2\x00\x00g2\x00\x00h2\x00\x00i2\x00\x00j2\x00\x00k2\x00\x00l2\x00\x00m2\x00\x00n2\x00\x00\xe88\x01\x00\x02\x00\x00\x00x\x05\x00\x00\x14\x05\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\x1e\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\xe2\x04\x00\x00x\x05\x00\x00\x14\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\x05\x00\x00\x00\x97\x04\x00\x00\x82\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00E7CA65090D658757_##\x00\x0e\x00\x00\x00GongBenWuZang\x00\x01\x14\x00\x00\x00C2F5E48F7D5C72F0_##\x00\x07\x00\x00\x00301300\x00L\x00\x00\x00Prefab_Characters/Prefab_Hero/130_GongBenWuZang/130_GongBenWuZang_actorinfo\x00\x01\x00\x00\x00\x01X\x1b\x00\x00\xd7\r\x00\x00=\x00\x00\x00\xaaG\x00\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x89\x00\x00\x00P\x00\x00\x00\xd8\x0e\x00\x00\xc0\xc6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00\xc0\xc6-\x00(\x17\x02\x00\x00\x00\x00\x00`[\x03\x00X\x0f\x02\x00\xd32\x00\x00\x00\x00\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xd22\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xdc2\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xe62\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00\x06\x00\x00\x00\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x00\x004744E357C306D3C2_##\x00\x01\x11\x00\x00\x00\x19\x00\x00\x00WrapperAI/Hero/HeroLowAI\x00\x1c\x00\x00\x00WrapperAI/Hero/HeroSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmNormalAI\x00"\x00\x00\x00WrapperAI/Hero/HeroFiveCampSimple\x00\x02\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00BB3239B9CC0563BF_##\x00\x02\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00200065368D0DBAAB_##\x00\x19\x00\x00\x00Play_bobao_gongbenwuzang\x00\x01\x00\x00\x002\x00\x00\x00Prefab_Characters/Prefab_Hero/commonresource/Born\x007\x00\x00\x00PrZ\xf9\xd8O\xb7F\x1bLuaS\x01\x19\x93\r\n\x1a\n\x04\x04\x08\x08xV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(w@\x01<@Assets/Prefabs/Lua/AOV/MagicLab/MagicLabRewardItemView.lua\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x14\x00\x00\x00\x03\x00@\x00N@\x00\x00\x83\x80@\x00\x93\xc0@\x01\x04\x80\x80\x01C\x00A\x00\x8e@\x01\x00D\x80\x00\x01\x8c\x00\x00\x00\x07\x80\x00\x83\x8c@\x00\x00\x07\x80\x80\x83\x8c\x80\x00\x00\x07\x80\x00\x84\x8c\xc0\x00\x00\x07\x80\x80\x84\x8c\x00\x01\x00\x07\x80\x00\x85\x0b\x00\x00\x01\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06Class\x04\x17MagicLabRewardItemView\x04\x02N\x04\x0bCUILuaView\x04\x08require\x04\x19AOV.MagicLab.MagicLabSys\x04\x0edocumentation\x04\rOnViewInited\x04\x08Refresh\x04\nSetCDNPic\x04\nItemClick\x01\x00\x00\x00\x01\x00\x05\x00\x00\x00\x00\x06\x00\x00\x00\r\x00\x00\x00\x01\x00\x02\x17\x00\x00\x00\x0b\x00\x80\x00C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S@\xc1\x00\x07@\x00\x80C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc1\x00\x07@\x00\x83C@@\x00S@\xc2\x00\x07@\x00\x84C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc2\x00\x07@\x00\x85\x0b\x00\x80\x00\x0c\x00\x00\x00\x04\x0cListElement\x04\x03CS\x04\x07Assets\x04\x08Scripts\x04\x03UI\x04\x15CUIListElementScript\x04\x07CDNpic\x04\x10CDNPicComponent\x04\x08BoxText\x04\x06Text2\x04\x0bClickEvent\x04\x0fCUIEventScript\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x01\x00\x00\x00\x05self\x00\x00\x00\x00\x17\x00\x00\x00\x01\x00\x00\x00\x05_ENV\x00\x0f\x00\x00\x00\x17\x00\x00\x00\x01\x00\x05\r\x00\x00\x00\x07@@\x80S\x80@\x00\x8c\x00\x00\x00G\x80\x80\x81S\x00A\x00l@\xc1\x00\xc3\x80A\x00\x03\xc1A\x00\x13\x01B\x02\xc4\x00\x00\x01D\x80\x00\x00G\x80\xc2\x84\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06BoxID\x13\xff\xff\xff\xff\xff\xff\xff\xff\x04\x0bClickEvent\x04\x08onClick\x04\x0cListElement\x04\rGetComponent\x04\x07typeof\x04\x02N\x04\x0fCUIEventScript\x04\x08enabled\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x00\x00\x02\x04\x00\x00\x00\x05\x00\x00\x00,\x00@\x00\x04@\x00\x01\x0b\x00\x80\x00\x01\x00\x00\x00\x04\nItemClick\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05self\r\x00\x00\x00\x10\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x14\x00\x00\x00\x16\x00\x00\x00\x16\x00\x00\x00name="_TargetPos" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="6c8555eb-3d65-40dc-b96b-22085a7b349f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.MSES\x07\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f36f7a0cf63b751b43487af3ac37a561\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00HB\x00\x00\xc8B\x14\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0A\x00\x00HB\x14\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00 A\x00\x00\xf0A\x14\x00\x00\x00\x14\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0@\x00\x00 A\x14\x00\x00\x002\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\xa0@\x14\x00\x00\x00d\x00\x00\x00\xf4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x14\x00\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x14\x00\x00\x00\xe8\x03\x00\x00\x88\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xd7\xa3=\x14\x00\x00\x00\x88\x13\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xccL=MSES\x07\x00\x00\x00^\x00\x00\x00\x06\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ea39319bc554c025c5f107f401c732b8\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00e\x00\x00\x00\x14\x00\x00\x00C235D3F892E815B5_##\x00\x14\x00\x00\x006E67E299EE10381A_##\x00\n\x00\x00\x00touxiang1\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00f\x00\x00\x00\x14\x00\x00\x008BD1A0FD4DFCA919_##\x00\x14\x00\x00\x005696820E83B5B08F_##\x00\n\x00\x00\x00touxiang2\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00g\x00\x00\x00\x14\x00\x00\x007B989B6E5EDFA305_##\x00\x14\x00\x00\x00498F4E0296"" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDeadControlHero" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCurrentTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMoveDirection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Angle" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBigMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyMe" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="bulletID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCantAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType1" valu\x00\x00\x00\x04\x00\x00\x00\x91\x00\x00\x00\x0b\x00\x00\x00Elementz\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_LOD3\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_Show1\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00]\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0f\x00\x00\x00SavedSkinId7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00CrossFadeTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.3\x04\x00\x00\x00\x04\x00\x00\x00#\x04\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\xc0\x03\x00\x00\x02\x00\x00\x00\xda\x01\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00~\x01\x00\x00\x02\x00\x00\x00)\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00x8\x00\x00\x00\x03 r="0.100" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack5" eventType="StopTrack" guid="b3cfc329-c442-4487-ab73-1d5ffcf3a8d7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.133" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="2" guid="d1939f1f-84aa-46f2-9322-abcc2231ad1a" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x120X\xbc\xa5S\x00\x00\xa5S\x00\x00#\x00\x00\x00196_Elsu/skill/AfterLastEvent="true">\n\t\t\t<Event eventName="HitTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="hitTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInheritRefParams" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="triggerId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bulletHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="victimId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="lastHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSkillCombineChoose" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="1841001" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" val\t<Vector3i name="offsetDir" x="0" y="0" z="0" refParamName="_TargetDir" useRefParam="true"/>\n\t\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="distance" value="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="18000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="gravity" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAdjustSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="1e0b1d40-f329-4718-b4d0-d5c0caaaa1e4" enabled="true" lod="0" useRefParam="false" refParamName="" r="1.000" g="0.233" b="me="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.650" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="1.267" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="clipName" value="Atk1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontReplaceSameAnim" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="subLayer" .Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00I\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe2\x00\x00\x00\x02\x00\x00\x00\x91\x00\x00\x00\x06\x00\x00\x00v1\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acA1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00O\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x97\x00\x00\x00\x06\x00\x00\x00v1\x85\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringW\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acmakeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9b\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x10\x01\x00\x00\x01\x00\x00\x00\x08\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa1\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00\x06\x00\x00\x00v1>\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x10\x00\x00\x00\x05\x00\x00\x00V6710002\x04\x00\x00\x00\x04\x004_##\x00>\x00\x00\x00\x1e\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002B5B6A1F7A9007E5_##\x00?\x00\x00\x00$\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00EE2974C205C472E7_##\x00\x01\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002521BBD3EE0BDF80_##\x00<\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x01<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":68}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00BDB77D73EF3CDFB6_##\x00\x03\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00898A75C147D555B3_##\x00\x06\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00FA3AF0603BDD9365_##\x00\x07\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x0051ED5D030B64764D_##\x00\n\x00\x00\x00\t\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00C50583CB6167E4E5_##\x00\x0b\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd8\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x004721F4D35F33FCA5_##\x00\x0c\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x00<\x00\x00\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00HF\xa6,D\x0e\x00\x00D\x0e\x00\x00+\x00\x00\x00177_ChengJiSiHan/skill/AutoChess/acA1E3.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList/>\n\t<Action tag="" length="0.300" loop="false">\n\t\t<Track trackName="SkillFuncDuratio-9322-abcc2231ad1a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.833" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticle" time="0.000" length="1.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet1" id="3" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<uint name="RefLiteBulletID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/174_yuji/yuji_attack01_spell02" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="dontShowIfNoBindPoint" valtem.Int32]\x04\x00\x00\x00\xeb\x00\x00\x00\x02\x00\x00\x00\x9a\x00\x00\x00\x06\x00\x00\x00v1\x88\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringZ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huijidi_dead\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00S\x0e\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xbb\r\x00\x00\x0b\x00\x00\x00\x1f\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb8\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x06\x00\x00\x00v28\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0b\x00\x00\x00\x05\x00\x00\x00V10\x04\x00\x00\x00\x04\x00\x00\x00@\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd9\x00\x00\x00\x02\x00\x00\x00\x88\x00\x00\x00\x06\x00\x00\x00v1v\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/109_daji/daji_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V3\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneSkillSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplaceHPBarImmuneSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCallBoss" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidExtraBtnSlot1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="43618e12-f288-4877-9d44-4cb1ef89f0a2" enabled="true" useRefParam="false" refParamName="" r="0.467" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.333" isDur1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/536_Ninja/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/544_Painter/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xc5z\x03\xef/\x0c\x00\x00/\x0c\x00\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81`\x00\x00\x00Prefab_Hero/544_Painter/544_Painter_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xe1\x00\x00\x00\xe0\x0c\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00Prefab_Hero/148_JiangZiYa/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00h-\x11\x99U\x1f\x00\x00U\x1f\x00\x007\x00\x00\x00Prefab_Hero/148_JiangZiYa/148_JiangZiYa_actorinfo.bytesU\x1f\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x01\x1f\x00\x00\x0f\x00\x00\x00]\x00\x00\x00\r\x00\x00\x00ActorNameD\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x16\x00\x00\x00\x05\x00\x00\x00V148_JiangZiYa\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xaf\x01\x00\x00\x03\x00\x00\x00\x8d\x00\x00\x00\x0b\x00\x00\x00Elementv\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplayWhenChangeMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTrailProtect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepChildScale" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/HeroStun\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x008\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x80\x00\x00\x00\x06\x00\x00\x00v1n\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String@\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x004\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcd\x00\x00\x00\x02\x00\x00\x00|\x00\x00\x00\x06\x00\x00\x00v1j\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xbc\x07\x00\x00\x0e\x00\x00\x00animationsw\x00\t\t<String name="SpecialActionName" value="prefab_characters/prefab_hero/115_gaojianli/skill/a1b2" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDeadRemove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmeExcute" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeEternal" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletTypeId" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletUpperLimit" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpawnBounceBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="bulletSkillType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\xbb\x98\xe8\xae\xa4\xe7\xb1\xbb\xe5\x9e\x8b_0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x81\xe8\xae\xb8\xe7\x89\xb9\xe6\xae\x8a\xe6\x89\x93\xe6\x96\xad_1"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDestroyedBySpecialBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTrigger\t\t\t\t<bool name="forbidFilterSkill4" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill5" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill6" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill7" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill8" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill10" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill11" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSummonerSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterMapSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterEquipActiveSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterActiveSame="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRealTimeSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOpenSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBlockObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkin" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRecordObjPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="recordTargeID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TrackObject name="trackId" id="-1" guid="00000000-0000-0000-0000-000000000000" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetCollisionTick0" eventType="SetCollisionTick" guid="dcd824ef-bb03-4fc8-bf5c-a64a29c3c0\t<int name="ExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Rotation" value="160" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="HeightGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="RotationGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</EMSES\x07\x00\x00\x00\x1c\x00\x00\x00\x0e\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009b0dbb76c4f9d3da6c78991155e5e1c2\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x05\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0c\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\r\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x91\xb0\x00\x00\x08\x00\x00\x00RargetSkillCombine_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_3" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBullet" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="BulletActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/extend/exs2b1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeImmeExcute" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTriggerObj" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceUseTriggerObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerMode" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBounceBullete"/>\n\t\t\t\t<int name="triggerInterval" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorInterval" value="30" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterFriend" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterMonter" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterChest" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEye" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMyself" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" \xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x85\xe9\x80\x9f\xe5\xa4\x8d\xe6\xb4\xbb"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe7\x90\x83\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\xa9\xb1\xe6\x95\xa3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x85\x8d\xe7\x96\xab\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe8\x8e\xb7\xe5\x8f\x96\xe8\xa7\x86\xe9\x87\x8e\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\xba\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9f\xa7\xe6\x80\xa7\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x86\xb7\xe5\x8d\xb4\xe7\xbc\xa9\xe5\x87\x8f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x97\xe6\x9a\xb4\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5RVO"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe6\x9d\xa1\xe4\xbb\xb6\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9b\xb4\xe6\x8d\xa2\xe8\xa1\x80\xe6\x9d\xa1\xe9\xa3\x8e\xe6\xa0\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\xbb\x8f\xe9\xaa\x8c\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xbb\x8f\xe9\xaa\x8c\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x97\xe6\x8e\xa7\xe9\xa2\x9d\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"<int name="level3Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level4Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level5Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level6Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOtherSkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillUseCacheTick0" eventType="SkillUseCacheTick" guid="53c33571-7838-484f-9f06-7b93d4bc28e0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.217" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillUseCacheTick" time="0.350" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="e8a22af8-4078-4313-893b-f729c0f328ed" enabled="false" useRalse"/>\n\t\t\t\t<bool name="bUseRealScaling" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseHeroLocalForward" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRandomRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="randRotBegin" x="0.ramName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="612800" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckCondition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOvertimeCD" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSendEvent" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="attackTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="level0Id" valuname="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x89\x80\xe6\x9c\x89\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bVaildBlockForSelfTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVaildBlockForEnemyTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Pos" x="0" y="0" z="-1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Size" x="2000" y="10000" z="3000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="PosList" refParamName="" useRefParam="false" type="Vector3i"/>\n\t\t\t\t<int name="Radius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorRadius" value="1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Height" value="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Degree" value="160" refP\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/commonresource/Dead_Born\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x003\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcc\x00\x00\x00\x02\x00\x00\x00{\x00\x00\x00\x06\x00\x00\x00v1i\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String;\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x000\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc9\x00\x00\x00\x02\x00\x00\x00x\x00\x00\x00\x06\x00\x00\x00v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/A1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x002\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcb\x00\x00\x00\x02\x00\x00\x00z\x00\x00\x00\x06\x00\x00\x00v1h\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String:\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/\x00h\x00\x00\x00\x01\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V2200\x04\x00\x00\x00\x04\x00\x00\x00g\x00\x00\x00\x0b\x00\x00\x00HudTypeP\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.HudCompType\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00n\x00\x00\x00\x11\x00\x00\x00collisionTypeQ\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum1\x00\x00\x00\x08\x00\x00\x00TypeNucleusDrive.Share.CollisionShapeType\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x01\x00\x00\x14\x00\x00\x00iCollisionCenter&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00x7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V200\x04\x00\x00\x00\x04\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00z7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1600\x04\x00\x00\x00\x04\x00\x00\x00v\x00\x00\x00\x12\x00\x00\x00BtResourcePathX\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String*\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Soldier/BTSoldierNormal\x04\x00\x00\x00\x04\x00\x00\x00\x8d\x00\x00\x00\x0f\x00\x00\x00deadAgePathramName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType2" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBeControledActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyAttackerPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyDeadOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCanntAttackOrgan" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorCount" value="32" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="SelectMode" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x9a\x8f\xe6\x9c\xba\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe8\xa1\x80\xe9\x87\x8f\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x89\xe7\x9c\xbc\xe7\x9a\x84\xe8\xa7\x84\xe5\x88\x99\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="CollideMaxCount" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" am="false" />\r\n        <bool name="bExtraBuff" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bOverrideParam" value="false" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam1" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam4" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam5" value="0" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId2" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabl guid="884649fb-eee1-4f09-8e8c-136817834eb9" enabled="true" useRefParam="false" refParamName="" r="0.900" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetBehaviourModeTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delayStopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="deadControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0="SkillInputCacheDuration" time="0.233" length="0.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCacheSkillReCalcLock" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkMoveAbortCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDure"/>\n\t\t\t\t<int name="animatorOverrideLayer" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLoop" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseFadeOutTime" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="fadeOutTime" value="0.200" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="startTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="endTime" value="99999.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeed" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alwaysAnimate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepOldSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCanNotBeCulled" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="beginClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayBeginCliTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/fireta_hurt_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00825732d46fb1b030cdac35cc22c3f23d\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x07\x00\x00\x00\x14\x00\x00\x00A409CCAC72376898_##\x00\x1c\x00\x00\x00\x1e\x00\x00\x00\x14\x00\x00\x000629BC043F5D2625_##\x00\x1c\x00\x00\x00d\x00\x00\x00\x14\x00\x00\x007D56267D87A29EDD_##\x00\x1c\x00\x00\x00m\x01\x00\x00\x14\x00\x00\x00DFB6F47F471FD135_##\x00\x13\x0f\x00\x00\x08\x00\x00\x00ROOTC\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom.\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSet\x04\x00\x00\x00\xc0\x0e\x00\x00\x01\x00\x00\x00\xb8\x0e\x00\x00\x0e\x00\x00\x00baseSubsetF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSubset\x04\x00\x00\x00\\\x0e\x00\x00\x04\x00\x00\x00l\x05\x00\x00\x0b\x00\x00\x00actionsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xe2\x04\x00\x00\x04\x00\x00\x005\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xce\x00\x00\x00\x02\x00\x00\x00}\x00\x00\x00\x06\x00\x00\x00v1k\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String=\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/Soldier1/skill/M1A1\x04\x00\x00\x00\x04\x00>\n\t\t\t\t<bool name="bTargetPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="targetPosition" x="0" y="0" z="0" refParamName="" useRefParam="true"/>\n\t\t\t\t<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveCollision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="recreateExisting" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="superTranslation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyTranslation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="translation" x="-600" y="1400" z="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableTag" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" va\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="c41c436a-6fd5-4207-a69b-f3ffebeadf55" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.583" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDonotAttackToMesh" valuSoundTick7" eventType="PlayHeroSoundTick" guid="a23129b2-cb41-44f8-93ff-cf6c2ceaf519" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="sourceId" objectName="None" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="eventName" value="Play_Meilin_Wanou_Skill_Hit_1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="use1P3PSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSkinSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="extraSkinId" refParamName="" useRefParam="false" type="uint"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xffZ\x87\xc0\xeaa\x00\x00\xeaa\x00\x00*\x00\x00\x00Prefab_Monster/137_SiMaYi_Pet/skill/A2.xml<?xLLY\x04\x00\x00\x00\x04\x00\x00\x00,\x00\x00\x00\x0b\x00\x00\x00Element\x15\x00\x00\x00\x01\x00\x00\x00\r\x00\x00\x00\x08\x00\x00\x00NULLY\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00A\x06\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe9\x05\x00\x00\x05\x00\x00\x00\x01\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb5\x01\x00\x00\x03\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x07\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb8\x01\x00\x00\x03\x00\x00\x00\x90\x00\x00\x00\x0b\x00\x00\x00Elementy\x00\x00\x00\x03\x00\x00\x00\t\t<bool name="abortFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterDamage" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMoveRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delaySkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="protectAbortLevel" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe4\xbf\x9d\xe6\x8a\xa4"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="ImmuneNegative" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" valu\n        <int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_1" value="523000" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID1Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID2Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID3Probability" value="0" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSight" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSkillLevel" value="false" refParamName="" useRefParam="false" />\r\n        <Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\r\n          <uint name="\xe6\x99\xae\xe6\x94\xbb" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd1" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd2" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd3" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd4" />\r\n \x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x0f\x03\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00w\x02\x00\x00\x02\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Bullet\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x006\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcf\x00\x00\x00\x02\x00\x00\x00~\x00\x00\x00\x06\x00\x00\x00v1l\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String>\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Hit\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\xbe\x00\x00\x00:\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00189d89e27401dc8d9af987c9418892f7\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xab\x00\x00\x00\x02\x00\x00\x00\x00\n\x00\x00\x005v5\xe5\x8c\xb9\xe9\x85\x8d\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00Param="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="ReplacementUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x89\xe6\xb0\xb4\xe5\x8a\xa0\xe9\x80\x9f\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="ReplacementSubUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe8\x90\xbd\xe5\x9c\xb0\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bNoDynamicLod" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMeshResouce" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true"/>\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.500" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceForbidding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkillAndHideBtn" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill3" valame="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="refSkillLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="compareOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterMajorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMinorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSoldier" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterOtherMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAddEffectCount" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="f1307d98-07[System.String,System.Int32]\x04\x00\x00\x00\xf2\x00\x00\x00\x02\x00\x00\x00\xa1\x00\x00\x00\x06\x00\x00\x00v1\x8f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Stringa\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_RedTower_High/skill/New_RedTower_High_A1E1_Slow\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75013\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xb4\x04\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00$\x04\x00\x00\x04\x00\x00\x00\x07\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa0\x00\x00\x00\x02\x00\x00\x00O\x00\x00\x00\x06\x00\x00\x00v1=\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0f\x00\x00\x00\x05\x00\x00\x00V750130\x04\x00\x00\x00\x04\x00\x00<TemplateObject name="VirtualAttachBulletId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseAttachBulletShape" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/502_astrid/astrid_natk01_hurt01" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="lifeTime" value="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="bindPointName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="bindRotOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x05\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\x9e\x00\x00\x00\x02\x00\x00\x00M\x00\x00\x00\x06\x00\x00\x00v1;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x05\x00\x00\x00VAtk2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00508_Zhadanren/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00508_Zhadanren/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x00508_Zhadanren/skill/extend/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x11\xe7\x15!\x06x\x00\x00\x06x\x00\x00#\x00\x00\x00508_Zhadanren/skill/extend/exA4.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t\t<TemplateObject objectName="bullet" id="2" isTemp="true"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="targetdir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Tram="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillCDTriggerTick0" eventType="SkillCDTriggerTick" guid="ed9f0f3d-9931-4fb8-a5fa-b455c6cbe800" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillCDTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSlotType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80'
ZSTD_LEVEL = 17 # or 19 idk

def usage() -> None:
    print("\nUsage:\n\t{} [option] <file 1 path> <file 2 path> ...".format(sys.argv[0]))
    print("option:")
    print("\t-h, --help\t\tShow this")
    print("\t-c, --compress\t\tCompress Zstd")
    print("\t-d, --decompress\tDecompress Zstd")

def main() -> None:
    print("\033[1;32m------------------------------------------------------------")
    print("\033[1;32m==============>\033[1;31mTool Giải mã & Mã hoá File AOV\033[1;32m<==============")
    print("\033[1;32m------------------------------------------------------------")
    print("\n  ")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {} \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")

if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()

def main() -> None:
    print("\n\033[1;32m------------------------------------------------------------")
    print("\n => Tiếp tục giải mã & mã hoá")
    print("\n------------------------------------------------------------")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcd", ["help", "compress", "decompress"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    if not args:
        args = (input(" 📂 \033[1;33mNhập thư mục : "), )

    args = set(args)
    for input_path in list(args):
        if os.path.isdir(input_path):
            args.discard(input_path)
            
            for entry in os.scandir(input_path):
                if entry.is_file():
                    args.add(entry.path)

    for input_path in args:
        input_blob = None
        try:
            with open(input_path, "rb") as f:
                input_blob = f.read()
        except FileNotFoundError:
            print("\n\033[1;31m ❌Lỗi!! Không thể tìm thấy thư mục \"{}\"!!!  ".format(input_path))
            continue

        if opts:
            opt, arg = opts[0]
        else:
            pos = input_blob.find(b"\x28\xb5\x2f\xfd")
            if pos != -1:
               opt = "-d"
               input_blob = input_blob[pos:]
            else:
                opt = "-c"
        
        zstd_mode = None
        try:
            if opt in ("-c", "--compress"):
                zstd_mode = "mã hoá"
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))

                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
            elif opt in ("-d", "--decompress"):
                input_blob = input_blob[input_blob.find(b"\x28\xb5\x2f\xfd"):]

                zstd_mode = "giải mã"
                output_blob = pyzstd.decompress(input_blob, pyzstd.ZstdDict(ZSTD_DICT, True))

            output_path = input_path
            with open(output_path, "wb") as output_file:
                output_file.write(output_blob)
        except pyzstd.ZstdError:
            print("\n\033[1;31m Bị lỗi {}  \"{}\" Xong!!".format(zstd_mode, input_path))
            continue
        print("\n\033[1;35m ✔️File được {} \"{}\" Xong!!! ".format(zstd_mode, input_path))
    
    print("\n\033[2;37m Đã hoàn thành!!")


if __name__ == "__main__":
    main()
    
    print("\n\033[1;33m ====> Đã hết 60 lượt của Tool, vui lòng mở lại Tool để tiếp tục làm việc📁 ")