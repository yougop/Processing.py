#Create a Tone / Note. As simple and clean as possible. Start here.

add_library('Minim')  #import Library

minim = Minim(this)  #Minim Object
out = minim.getLineOut()  #Output
        
class SawInstrument(Instrument):
    def __init__(self, frequency):
        self.wave = Oscil(frequency, 0, Waves.SAW)  #Amplitude is useless because Line()
        self.ampEnv = Line()  #Line transition
        self.ampEnv.patch(self.wave.amplitude)        
    def noteOn(self, duration):
        self.ampEnv.activate(duration, 0.5, 0.5)  #Duration / Begin Amp / End Amp
        self.wave.patch(out)        
    def noteOff(self):
        self.wave.unpatch(out)
    
def setup():
    size(512, 200)   
    stroke(255)
    strokeWeight(1)     
    
    freq = 15; dur = 0.25  #Frequency and Durytion
    out.playNote( 0.0, dur, SawInstrument( freq ) )  #Play Note
    out.playNote( 1.0, dur, SawInstrument( freq ) )
    out.playNote( 2.0, dur, SawInstrument( freq ) )
    out.playNote( 3.0, dur, SawInstrument( freq ) )

def draw():
    background(60)
    for i in range(out.bufferSize() - 1):
        line(i, 50 - out.left.get(i) * 50, i + 1, 50 - out.left.get(i + 1) * 50)
        line(i, 150 - out.right.get(i) * 50, i + 1,150 - out.right.get(i + 1) * 50)
    
