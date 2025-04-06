# AA_Tournament


# Tournament Strategy: Name Amen
## Strategy Overview

The `name_amen` strategy is an adaptive approach to the **Iterated Prisoner's Dilemma (IPD)**, which is designed to both **exploit cooperative players** and **punish aggressive ones**. It combines features of well-known strategies, such as **Tit for Tat** (TFT) and **Grim Trigger**, but with additional complexity to make it more versatile.

### Key Features

1. **Initial Cooperation**:
   - The strategy always starts by cooperating in the first few rounds (this can be adjusted).
   
2. **Mode Switching**:
   - The strategy switches between different "modes" depending on the behavior of the opponent. These modes dictate how the strategy will respond in subsequent rounds.
     - **`full_defect`**: If the opponent defects continuously in the first five rounds, `name_amen` will switch to the `full_defect` mode, where it will always defect in future rounds. This mode is useful for dealing with opponents who always defect and are not worth cooperating with.
     - **`exploit`**: If the opponent cooperates in all the first five rounds, `name_amen` will switch to the `exploit` mode, where it will take advantage of the opponent's cooperation while avoiding being taken advantage of.
     - **`mixed`**: If the opponent shows a mix of cooperation and defection in the first five rounds, `name_amen` will switch to the `mixed` mode. In this mode, the strategy maintains a flexible approach, alternating between cooperation and defection depending on the opponent's previous moves.

3. **Dynamic Decision-Making**:
   - After the first five rounds, the strategy continues to evaluate the opponent’s behavior, switching between modes when appropriate.
   - **Punishment and Forgiveness**: 
     - If the opponent defects, the strategy might defect in response to prevent being exploited.
     - If the opponent cooperates, the strategy might reciprocate and continue cooperating.
     - In the `exploit` mode, the strategy will cooperate for a few rounds to maintain the opponent’s trust but will defect periodically to maximize its score.

4. **Periodic Adjustments**:
   - Every 6th round, the strategy might defect, even if the opponent has been cooperating. This prevents the opponent from taking advantage of the strategy by exploiting it in the long term.
   
5. **Behavior Against Other Strategies**:
   - **vs. Tit for Tat**: The strategy can outperform Tit for Tat by strategically switching between cooperation and defection, avoiding being trapped in endless cycles of retaliation.
   - **vs. Always Cooperate**: It exploits this strategy by defecting strategically to maximize the score.
   - **vs. Always Defect**: It responds by defecting from the start, ensuring that it doesn't lose points unnecessarily.

---

### Summary of Strategy Logic:

- **Starting Strategy**: Cooperate initially.
- **Behavior Change Based on Opponent**:
  - **Full Defect**: Defect constantly against defectors.
  - **Exploit**: Cooperate to gain the opponent's trust and defect strategically.
  - **Mixed**: Adaptively switch between cooperation and defection.
- **Punishment and Forgiveness Mechanisms**: React to aggression with retaliation, and cooperate to build alliances when possible.
