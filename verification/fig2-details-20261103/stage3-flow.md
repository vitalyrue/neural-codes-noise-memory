# Stage 3: Figure 2 connected reading

Local request ID: fig2-stage3-20261103. Reviewer: fig2_edit_review. Requested after the separate Stage 2 call. SEM recheck finished first in this call; the connected passages were then reread. No source edits or builds.

UTC start: 2026-11-03T17:53:55Z
UTC end: 2026-11-03T17:54:53Z
Wall-clock duration: 58 seconds
Awake execution time: unverified.

Scope: 02b Figure 1 introduction through the Figure 2 explanation and the information-chapter handoff; 11 mutual-inhibition setup through the measurement formula, its interpretation and the next supporting-text example. A targeted prerequisite reread covered 01-foundations lines 288-292. This is a local teaching review, not whole-book acceptance.

Reviewed SHA256 hashes:
- `content/chapters/02b-memory-long-delays.md`: `5A81E4F76DD1B221D30729C307AAA0B20E04E09A32C7BF90C8A120528FA3EBA3`
- `content/chapters/11-simulating-memory.md`: `D907DA29338C9045DC020DB361CF4111E5CA477BBF4012EB3F70882D114F9AFB`
- Rule source, pedagogy-language-contract.md: `F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A`

## Paragraph purposes and connections

All locations below bind to the source hashes above. Retain all these passages for the reasons recorded.

| Passage | Contribution and connection |
|---|---|
| 02b, Figure 1A introduction | Gives the earlier return-flow construction a visible state change. Prepares the distinction between a changed memory and an uncertain reading. |
| 02b, Figure 1B introduction and its two bullets | Defines the activity bump and identifies storage motion versus finite-spike uncertainty as separate errors. The later Figure 2 explanation explicitly follows the storage-motion branch. |
| 02b, information/readout links before original Figure 1 | Gives the other error a destination rather than treating Figure 2 as a test of both errors. The original-figure disclosure supports inspecting that explanation. |
| 02b, Figure 2A introduction | Announces a simulation test and identifies the ring arrangement before B uses neural position on that ring. The definition of rotational symmetry explains what the second network will change. |
| 02b, B | Moves from neural-index rate curves and spike marks to the represented angular trace. Distinguishing the 10-second separation from the 10-ms spike windows prevents conflating two different timescales. The final sentence connects preserved activity with changing memory. |
| 02b, C/D list introduction | Makes the short-interval and long-interval comparisons separate questions. |
| 02b, C bullet | Identifies which curve is a simulation, prediction or bound. The newly explained SEM makes trial uncertainty readable before the error bars are interpreted. It prepares D by saying the bar convention applies to both panels. |
| 02b, D bullet | Extends the comparison to long intervals and explains why the angular error saturates. The earlier wrapped-density calculation supplies pi squared divided by 3, so this sentence is a supported reminder. |
| 02b, E | Changes network architecture and stored coordinate together: two opposing population rates replace bump position. Naming a nonperiodic rate difference before F prevents reading its trace as another angle. |
| 02b, F | Assigns a physical meaning to the large rate scale and to each population. G can then square a change in their difference without ambiguity over what the vertical coordinate measures. |
| 02b, G | Turns the traces into a lag-dependent statistic, identifies both axes and the theory comparison, and sends exact reproduction details to 11. Its last sentences explain why the second network was useful and limit what these simulations establish. |
| 02b, original Figure 2 disclosure and final handoff | The figure remains available after its guided reading. The final handoff returns from model tests to D and raises the information-bound question already foreshadowed by C and Figure 1. It does not introduce a new unrelated objective. |
| 11, second-network introduction | Reminds the reader what the physical stored quantity is and why this example follows the ring: the theory applies beyond rotational symmetry. |
| 11, Methods/settings paragraph | Supplies the parameters needed for this particular reproduction and explains the large rates as population totals. This prepares the coordinate and scale conversion. |
| 11, activation/rate conversion paragraph | Separates theta_s from theta_r, supplies the tau relation and its squared effect on D, and warns that population spike generation cannot copy the ring update unchanged. These points explain both measurement units and an implementation limit before a reproduction uses them. |
| 11, measurement setup plus displayed equation | Names the plotted coordinate, total recording duration and lag before the equation combines them. It measures the change of r1 minus r2 across an interval, not either rate alone. The finite-time bounds say which starts remain available. |
| 11, hat/time-average paragraph | Explains the finite estimate and gives the 2-second/198-second trace. The overlap sentence distinguishes many intervals from independent trials and connects back to the separately explained ring SEM. |
| 11, units/prediction paragraph | Converts the numerical result into G's published units and tells the reader which diffusion coefficient belongs in the theoretical line. The final statement gives agreement its model-specific meaning. |
| 11, next supporting-text example | Clearly changes to a mutually excitatory pair and state-dependent diffusion. Its link sends the derivation and discrepancy discussion to the existing earlier treatment, so this transition does not require an untaught derivation here. |

## Reader-path answers

- **What is physically stored?** On the ring, the position of a population activity peak stores an angle. In the pair, the difference between summed population rates stores a nonperiodic value. The prose states this before graph interpretation depends on it.
- **What do the axes mean?** B distinguishes neuron index in the inset from time in the main trace. F uses inverse milliseconds for rates; G uses lag in seconds and squared inverse milliseconds for its MSD. C and D use angular squared displacements. The generic MSD-axis and lag teaching is available in 01-foundations:288-292, where lag is explicitly the separation of observations rather than start time.
- **What calculation produces G?** The named theta_r equals r1 minus r2. The equation subtracts its beginning value from its ending value, squares the change and averages over valid starting times. The following prose walks through those steps and a concrete lag. It supplies the interpretation rather than requiring an expert to infer it from brackets and a hat.
- **Which D and units belong together?** The preceding activation/rate paragraph explicitly gives theta_r = theta_s/tau and D_r = D_s/tau squared. The following units paragraph converts squared rates and uses D_r in 2 D_r times lag. The reader is warned before comparing numerical values from the two coordinates.
- **How do finite time and repeated trials differ?** T is the total 200-second trace. Valid starts stop at T minus lag. Overlapping intervals are identified as dependent. The ring comparison separately uses the uncertainty of a mean estimated over 100 trials. These are different averaging procedures in the text itself.
- **Does reading require filling a gap from outside expertise?** No for these Figure 2 additions and connected passages. Core lag/MSD meaning is taught in the checked foundations passage; wrapping and the saturation result are taught earlier in 02b; the local passages supply the neural rate meanings, coordinate conversion and finite-recording interpretation. No new method or source claim was supplied by the reviewer to complete an absent explanation.

## Outcome

Stage 3 passes for the reviewed connected passages. No required flow or teaching gap found. The separate SEM recheck records a duplicate later first-definition marker; it does not affect this connected-reading result. No unrelated chapter or whole-book quality claim is made.

Token stats unavailable.
