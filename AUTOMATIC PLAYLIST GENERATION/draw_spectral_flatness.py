import matplotlib.pyplot as plt
l1_1 = [0.06422975783546765, 0.07351303845643997, 0.05338668450713158, 0.07313144952058792, 0.03742324560880661, 0.0673869252204895, 0.05470277741551399, 0.08455353230237961, 0.03826340287923813, 0.07419796288013458, 0.1433667540550232, 0.09871679544448853, 0.08647959679365158, 0.05457165837287903, 0.07933811843395233, 0.0788498967885971, 0.08415137231349945, 0.04988589137792587, 0.07536272704601288, 0.062175165861845016, 0.08877904713153839, 0.04604293033480644, 0.07572411000728607, 0.07003146409988403, 0.0782916396856308, 0.050656773149967194, 0.09359998255968094, 0.07134078443050385, 0.05141616612672806, 0.04934902861714363, 0.065639428794384, 0.07312067598104477, 0.054787375032901764, 0.05408692732453346, 0.05857064202427864, 0.07318222522735596, 0.05368805676698685, 0.052580758929252625, 0.054713938385248184, 0.06490734219551086]
l1_2 = list(range(1,len(l1_1)+1))
l2_1 =[0.05763593688607216, 0.008701073937118053, 0.006447202060371637, 0.009558149613440037, 0.0029604178853332996, 0.00851516891270876, 0.004542151466012001, 0.010904425755143166, 0.0024520002771168947, 0.008819141425192356, 0.0046181827783584595, 0.009725107811391354, 0.004737741779536009, 0.009782101027667522, 0.01935451105237007, 0.013388009741902351, 0.00712219811975956, 0.012473901733756065, 0.006465298123657703, 0.00825381651520729, 0.005238322541117668, 0.009207348339259624, 0.0048675560392439365, 0.009237349033355713, 0.004153436981141567, 0.009093978442251682, 0.004955634940415621, 0.007589676883071661, 0.005523062311112881, 0.009428875520825386, 0.020162444561719894, 0.013364728540182114, 0.004577795974910259, 0.009912745095789433, 0.006626494228839874, 0.011130445636808872, 0.0033644200302660465, 0.012324524112045765, 0.005069761071354151, 0.010861240327358246, 0.0021725541446357965, 0.011523673310875893, 0.01296367309987545, 0.010774648748338223, 0.006095391232520342, 0.02201208844780922, 0.03595254570245743, 0.13357026875019073, 0.05734126269817352, 0.06254490464925766, 0.012431798502802849, 0.0571291446685791, 0.0925062969326973, 0.023459358140826225, 0.005562938284128904, 0.032172586768865585, 0.06070653349161148, 0.02043888531625271, 0.01554287038743496, 0.07671645283699036, 0.04481061175465584, 0.06028560549020767, 0.047334421426057816, 0.17423033714294434, 0.07692708820104599, 0.07988478988409042, 0.02257343754172325, 0.08067673444747925, 0.10184085369110107, 0.03620016574859619, 0.021917060017585754, 0.07262902706861496, 0.09264496713876724]
l2_2 =list(range(1,len(l2_1)+1))
l3_1 =[0.13974987715482712, 0.09809021651744843, 0.1254386007785797, 0.03924853727221489, 0.03377411514520645, 0.043848391622304916, 0.02790621854364872, 0.040756307542324066, 0.06440598517656326, 0.05071384087204933, 0.042764753103256226, 0.05482267215847969, 0.04456183686852455, 0.05172072723507881, 0.10740861296653748, 0.04674012213945389, 0.0559673085808754, 0.030491406098008156, 0.04483293369412422, 0.0836404487490654, 0.03199538215994835, 0.08050164580345154, 0.05446656048297882, 0.03975149244070053, 0.05636177584528923, 0.07000848650932312, 0.0674813762307167, 0.06143474578857422, 0.050607841461896896, 0.030203988775610924, 0.0555095337331295, 0.05602153018116951, 0.05869670584797859, 0.15005835890769958, 0.031155675649642944, 0.01882774941623211, 0.1416848599910736, 0.05163631588220596, 0.03983941674232483]
l3_2 =list(range(1,len(l3_1)+1))
l4_1 =[0.040296132365862526, 0.02849668823182583, 0.033829934895038605, 0.034057796001434326, 0.01695566438138485, 0.011571316979825497, 0.01372300274670124, 0.011130338534712791, 0.015743738040328026, 0.015250981785356998, 0.017836757004261017, 0.016044948250055313, 0.013636800460517406, 0.018787989392876625, 0.07597596943378448, 0.013833461329340935, 0.011462663300335407, 0.004124143626540899, 0.010695673525333405, 0.0016627948498353362, 0.00666113430634141, 0.0015687153209000826, 0.009838152676820755, 0.00164761149790138, 0.0077395690605044365, 0.0019300072453916073, 0.01084929145872593, 0.00131398590747267, 0.00728560471907258, 0.001199431368149817, 0.009925234131515026, 0.0028033852577209473, 0.008746825158596039, 0.0034876903519034386, 0.10920097678899765, 0.004484840203076601, 0.007207079324871302, 0.0017874023178592324, 0.07447066903114319, 0.004496775101870298, 0.00983259454369545, 0.004136768169701099, 0.007615720387548208, 0.0026196560356765985, 0.008845529519021511, 0.005605138372629881, 0.0148482546210289, 0.017626268789172173, 0.013933626003563404, 0.008081184700131416, 0.013325599022209644, 0.00541546568274498, 0.011996966786682606, 0.0034613097086548805, 0.014642560854554176, 0.004261953290551901, 0.01137798186391592, 0.007082871161401272, 0.012966198846697807, 0.00446113757789135, 0.009379129856824875, 0.004005881957709789, 0.012686227448284626, 0.00678593385964632, 0.013135614804923534, 0.00653431098908186, 0.013340266421437263, 0.006929459981620312, 0.011793549172580242, 0.00695799058303237, 0.02069956623017788, 0.00638079596683383, 0.012918638996779919, 0.005746711511164904, 0.009965303353965282, 0.0053477175533771515, 0.01370837353169918, 0.028642740100622177, 0.01491221971809864]
l4_2 =list(range(1,len(l4_1)+1))
l5_1 =[0.11369587232669194, 0.056150082498788834, 0.0456598699092865, 0.04373544082045555, 0.04287509247660637, 0.04684454947710037, 0.03445051610469818, 0.04519295692443848, 0.10129006206989288, 0.13351599872112274, 0.056200530380010605, 0.04583955556154251, 0.05765761062502861, 0.035665906965732574, 0.034461863338947296, 0.03980878368020058, 0.042249150574207306, 0.031766749918460846, 0.053014662116765976, 0.031770970672369, 0.07776730507612228, 0.06222747638821602, 0.04923613741993904, 0.04811318218708038, 0.07799510657787323, 0.052880700677633286, 0.09239964932203293, 0.06765671074390411, 0.05184023827314377, 0.05019496753811836, 0.045079171657562256, 0.07772474735975266, 0.08733639866113663, 0.052937205880880356, 0.0547320730984211, 0.05338940769433975, 0.0611380971968174, 0.05274214595556259, 0.044906243681907654, 0.04194048047065735, 0.11286605149507523, 0.12904641032218933, 0.0794900506734848, 0.040795452892780304, 0.05081857368350029, 0.03294375538825989, 0.022130701690912247, 0.024813439697027206, 0.026457302272319794, 0.024754280224442482, 0.02930542081594467, 0.019565461203455925, 0.014802004210650921]
l5_2 =list(range(1,len(l5_1)+1))
l6_1 =[0.004872758562366168, 0.005582528188824654, 0.0026300952304154634, 0.024187425151467323, 0.0013698764378204942, 0.0041226474568247795, 0.0010037034517154098, 0.005899854935705662, 0.0013130799634382129, 0.0003999528125859797, 0.0020189175847917795, 0.0071519468910992146, 0.001670086057856679, 0.004041999112814665, 0.021808883175253868, 0.01149262860417366, 0.003592677414417267, 0.07137175649404526, 0.003760602790862322, 0.004391913767904043, 0.017295921221375465, 0.007352679036557674, 0.002884301822632551, 0.007271959446370602, 0.0035244307946413755, 0.001069315942004323, 0.0019113809103146195, 0.005646029487252235, 0.00325508089736104, 0.003919643349945545, 0.006456105504184961, 0.006582885514944792, 0.0036675864830613136, 0.0017518281238153577, 0.004057544283568859, 0.0016181167447939515, 0.0017181141301989555, 0.005318072158843279, 0.031186969950795174, 0.007421326357871294, 0.0019522414077073336, 0.0023790246341377497, 0.001904916251078248, 0.003706950694322586, 0.005114868748933077, 0.001848072512075305, 0.00435133371502161, 0.00428351666778326, 0.003655009903013706, 0.0024815963115543127, 0.0009147544042207301, 0.001040323986671865, 0.001658377586863935, 0.005377335473895073, 0.003228890709578991, 0.006551397033035755, 0.0009255465120077133, 0.0016404564958065748, 0.03267376124858856, 0.0027386213187128305, 0.0028248524758964777]
l6_2 =list(range(1,len(l6_1)+1))
l7_1 =[0.028361278896530468, 0.033847875893116, 0.035385239869356155, 0.003797330427914858, 0.051829054951667786, 0.003130406141281128, 0.014252581633627415, 0.020747318863868713, 0.08167460560798645, 0.010836182162165642, 0.08073551952838898, 0.02856692485511303, 0.014445171691477299, 0.004998546093702316, 0.023075835779309273, 0.0037743751890957355, 0.02096245065331459, 0.004812455270439386, 0.03195913881063461, 0.004478536546230316, 0.07777883112430573, 0.014993522316217422, 0.013071012683212757, 0.006684259511530399, 0.05067334324121475, 0.00432935543358326, 0.01371808722615242, 0.008822460658848286, 0.02146282233297825, 0.0046217474155128, 0.029183797538280487, 0.016456572338938713, 0.052488479763269424, 0.018939340487122536, 0.04009467735886574, 0.004922461695969105, 0.02397187054157257, 0.0037545643281191587, 0.022273709997534752, 0.009790713898837566, 0.0709860622882843, 0.00441371276974678, 0.055745989084243774]
l7_2 =list(range(1,len(l7_1)+1))
l8_1 =[0.012947092143197855, 0.008105607703328133, 0.015138845890760422, 0.01332774106413126, 0.005708407144993544, 0.0020504158455878496, 0.1735105663537979, 0.00331590767018497, 0.07898695766925812, 0.017186548560857773, 0.001543268095701933, 0.0021637962199747562, 0.006542475428432226, 0.0031626266427338123, 0.0003318593662697822, 6.388768088072538e-05, 1.0793472938530613e-05, 0.005072922445833683, 0.10035213828086853, 0.0022154352627694607, 0.10069331526756287, 0.0003653736785054207, 0.0015671122819185257, 0.0011885609710589051, 0.1085120141506195, 0.10468403249979019, 0.04439177364110947, 0.001031802617944777, 0.0015482757007703185, 0.0014468241715803742, 2.403247526672203e-05, 4.943859039485687e-06, 5.708702701667789e-06, 0.002142006531357765, 0.12458592653274536, 0.002900330349802971, 0.00044372756383381784, 0.1060796007514, 0.10148949176073074, 0.0009179964545182884, 0.0008676786674186587, 0.00021927121269982308, 0.0007321099401451647, 0.07609080523252487, 0.1381015181541443, 0.002052387921139598, 0.0006166118546389043, 0.001585791353136301, 0.0007170687895268202, 0.01946924813091755, 0.00023745132784824818, 0.10209420323371887, 0.005843267310410738, 0.0008862228132784367, 0.006676319986581802]
l8_2 =list(range(1,len(l8_1)+1))
l9_1 =[0.018711030250415206, 0.07173844426870346, 0.000729635008610785, 0.005182280670851469, 0.0005693898419849575, 0.09943089634180069, 0.0007489269482903183, 0.00045779134961776435, 0.0009540010942146182, 0.0013412010157480836, 0.000198564215679653, 0.0023981838021427393, 0.017400680109858513, 0.03339870274066925, 0.005941849667578936, 0.001154154073446989, 0.0006741681136190891, 0.0007982510142028332, 0.04283347725868225, 0.000981634366326034, 0.0006073686527088284, 0.0017952994676306844, 0.0011931759072467685, 0.0008389477152377367, 0.0003899534640368074, 0.0019847291987389326, 0.004184086807072163, 0.017906125634908676, 0.0012259010691195726, 0.002122457604855299, 0.003966209478676319, 0.001140266889706254, 0.0018583361525088549, 0.0010960036888718605, 0.000497799483127892, 0.0036828191950917244, 0.0012911773519590497, 0.0005230458918958902, 0.00065993593307212, 0.0003163851797580719, 0.00029339062166400254, 0.0010473123984411359, 0.055782970041036606, 0.015213066712021828, 0.09199679642915726, 0.10090015083551407, 0.06943254172801971, 0.0007003745413385332, 0.0002622462634462863, 0.0007345117628574371, 0.04759282246232033, 0.0010594554478302598, 0.0013774624094367027, 0.0018507424974814057, 0.0016995592741295695, 0.0011973901418969035, 0.0022921054624021053, 0.0012638098560273647, 0.002673483919352293, 0.036049339920282364, 0.0017702864715829492, 0.002021590480580926, 0.015500311739742756, 0.0014592070365324616, 0.0008066969458013773]
l9_2 =list(range(1,len(l9_1)+1))
l10_1 =[0.029027801181655377, 0.06944870203733444, 0.001087668351829052, 0.11584141105413437, 0.07992728054523468, 0.0004605101130437106, 0.018033461645245552, 0.0008706197259016335, 0.0023114534560590982, 0.14313353598117828, 0.0016080724308267236, 0.0014863194664940238, 0.003158208914101124, 0.0013136102352291346, 0.0019184513948857784, 0.01180863007903099, 0.0028869258239865303, 0.008822192437946796, 0.002846234245225787, 0.001970228273421526, 0.001273185946047306, 0.019480956718325615, 0.0010309446370229125, 0.0004210924671497196, 0.16146264970302582, 0.0013122333912178874, 0.007224678061902523, 0.0033972528763115406, 0.12536267936229706, 0.009319967590272427, 0.1380251795053482, 0.006916211452335119, 0.05364144593477249, 0.024511581286787987, 0.01025195512920618, 0.09805070608854294]
l10_2 =list(range(1,len(l10_1)+1))
colors1 = '#00CED1' #点的颜色
colors2 = '#DC143C'
# plt.scatter(l1_2,l1_1, c=colors1, alpha=0.4, label='1')
# plt.scatter(l2_2,l2_1, c=colors1, alpha=0.4, label='2')
plt.scatter(l3_2,l3_1, c=colors1, alpha=0.4, label='1')
# plt.scatter(l4_2,l4_1, c=colors1, alpha=0.4, label='4')
# plt.scatter(l5_2,l5_1, c=colors1, alpha=0.4, label='5')
plt.scatter(l6_2,l6_1, c=colors2, alpha=0.4, label='2')
# plt.scatter(l7_2,l7_1, c=colors2, alpha=0.4, label='7')
# plt.scatter(l8_2,l8_1, c=colors2, alpha=0.4, label='8')
# plt.scatter(l9_2,l9_1, c=colors2, alpha=0.4, label='9')
# plt.scatter(l10_2,l10_1, c=colors2, alpha=0.4, label='10')
plt.legend( loc = (0.95, 0.9))
plt.show()#这个智障的编辑器