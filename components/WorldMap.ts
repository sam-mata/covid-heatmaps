import * as Plot from "@observablehq/plot";
import {h} from "vue";

export default {
    props: ['options'],

    render() {
        Plot.plot({
            projection: "equal-earth",
            marks: [
                Plot.graticule(),
                Plot.text(["London", -0.1, 51.5]),
                Plot.sphere()
            ]
        })
    }
}
