# MAX98357AETE

[音频功率放大器](https://www.jlc-smt.com/lcsc/detail?componentCode=C910544)

D级运放

重点
SD_MODE# 下拉到地关断, (I2S LJmode)-> data channel
(TDM mode)-> SD_MODE# & GAIN_SLOT -> channel selection

SD_MODE STATUS                                      SELECTED CHANNEL
VSD_MODE > B2 trip point(1.4V)                    Left
B2 trip point > VSD_MODE > B1 trip point(0.77V)    Right
B1 trip point > VSD_MODE > B0 trip point(0.16V)    (Left/2 + right/2)
B0 trip point > VSD_MODE                            Shutdown


Vref * RL / (RH + RL) = Vo
RH = (Vref * RL / Vo) - RL
当RL = 100K, Vref = 3.3V
(3.3 + 1.4)/2 = 2.35 => 40K (这个直接接VDD而不是40K)
(1.4 + 0.77)/2 = 1.085 => 204K
(0.77 + 0.16)/2 = 0.465 => 609K


GAIN_SLOT
GND GND(100K) float VDD(100K) VDD

GAIN_SLOT    I2S/LJ GAIN (dB)
GND(100K) 15dB
GND         12dB
flaot       9
VDD         6
VDD(100K)   3

I2S Digital Audio Interface
LRCLK
BCLK
DIN