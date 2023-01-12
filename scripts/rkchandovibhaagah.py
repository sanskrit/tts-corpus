import os
import re

padyam = '../accented/padyam'
rksamhitaa = padyam + '/shakala-saMhitA'

rksaatih = re.compile(r'(?s)## ([0-9]{2}) [^-]+ - ([^\n]+)\n.+?\n\n([ँ-।१३\[\] \n]+॥)', re.MULTILINE)

sankhyaa = 0

for i in range(1,11):
	mandalam = str(i).rjust(2,'0')
	mandala_sthaanam = os.path.join(rksamhitaa, mandalam)
	for s in [f for f in os.listdir(mandala_sthaanam) if f[0] != '_']:
		suuktam = open(os.path.join(mandala_sthaanam, s)).read()
		purvyah_kramah = 0
		for rk in rksaatih.finditer(suuktam):
			sankhyaa += 1
			rk_kramah = rk.group(1)
			try:
				assert int(rk_kramah) == purvyah_kramah + 1
				purvyah_kramah += 1
			except AssertionError:
				print(f'mandalam: {mandalam}, suuktam: {s.split(".")[0]}, purvyah_kramah: {purvyah_kramah}, rk_kramah: {rk_kramah}')
			chandah = rk.group(2)
			muulam = rk.group(3)
			if '[' in muulam:
				muulam = muulam.replace(re.findall(r'\[.+\]', muulam)[0], '') # 07/023.md:907: स नः॑ स्तु॒तो वी॒रव॑त्पातु॒ [वी॒रव॑द्धातु॒] गोम॑द्यू॒यं पा॑त स्व॒स्तिभिः॒ सदा॑ नः ॥
			chandah_sthaanam = os.path.join(padyam, chandah)
			if not os.path.exists(chandah_sthaanam):
				os.mkdir(chandah_sthaanam)
			with open(os.path.join(chandah_sthaanam, f'{mandalam}_{s.split(".")[0].split("_")[0]}_{rk_kramah}.md'), 'w+') as f: # 086_vRShAkapiH.md, 10/189_AyaM_gauH.md इति॒ क्समा॑द् ए॒वं लि॑खि॒ते इ॒मे?
				f.write(muulam)

assert sankhyaa == 10552